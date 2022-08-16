##################################################
# FILES : ex11.py
# WRITER : Omer Ferster , omerferster , 206893653
# EXERCISE : intro2cse ex11 2021
# DESCRIPTION: A DECISION TREE GAME
##################################################

from itertools import combinations


class Node:

    """
    A Node class, each Node represent A node in the binary Tree decision.
    data field: An Yes/No question or An solution if the node is A leaf
    positive_child field: The following Node answering Yes for the question
    negative_child field: The following Node answering No for the question
    """

    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

    def is_illness(self):
        """
        The function finds if a current Node is An illness
        :return: True if the Node is a leaf, False otherwise
        """
        if self.positive_child is None and self.negative_child is None:
            return True
        return False


class Record:

    """
    A Record class, representing records of illnesses and it symptoms
    illness field: A string of the current illness
    symptoms field: A list of strings, shows the symptoms of specific illness
    """

    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    """
    The function finds each illness and it symptoms from a given file
    :param filepath: The file, contains info about illnesses names & symptoms
    :return: A list of Records objects, each element inside the list contains
    The name of the illness and it specific symptoms
    """
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:

    """
    The Diagnoser class, contains A Tree of Nodes, each Node represent A
    symptom & every leaf represent An illness that fits the current path of
    symptoms in the Tree. The class handles features as: diagnose an illness
    according given symptoms, find all possible illnesses & paths etc ...
    """

    def __init__(self, root):
        self.root = root

    def _diagnose_helper(self, current, symptoms):
        """
        An helper function, finds A fitting illness according the symptoms
        :param current: A specific symptom we're checking
        :param symptoms: A list of strings, shows all the symptoms given
        :return: A fitting illness answering all symptoms given
        """
        if current.is_illness():
            return current.data  # base case, found An illness
        if current.data in symptoms:
            return self._diagnose_helper(current.positive_child, symptoms)
        if current.data not in symptoms:
            return self._diagnose_helper(current.negative_child, symptoms)

    def diagnose(self, symptoms):
        """
        The function finds which illness fits the symptoms given
        :param symptoms: A list of strings, representing the illness symptoms
        :return: An illness, A leaf Node fits the given symptoms
        """
        return self._diagnose_helper(self.root, symptoms)  # using helper

    def calculate_success_rate(self, records):
        """
        The function finds the success rate of diagnose method
        :param records: A list of Records objects
        :return: The division between successful diagnoses & Records list len
        """
        if len(records) == 0:
            raise ValueError('Records list must contain at least 1 record')
        else:
            counter = 0  # A counter of successful diagnoses
            for record in records:
                check_illness = self.diagnose(record.symptoms)
                if check_illness == record.illness:
                    counter += 1  # found a correct diagnose
            return counter / len(records)

    def _find_all_illnesses(self, current, result):
        """
        The function finds all illnesses in the Tree
        :param current: The current Node to check
        :param result: The returned result list with all illnesses inside it
        :return: A list with all illnesses in the Tree, with repetitions
        """
        if current.is_illness() and current.data is not None:
            result.append(current.data)  # base case, found An illness
            return
        if current.positive_child is not None:
            self._find_all_illnesses(current.positive_child, result)
        if current.negative_child is not None:
            self._find_all_illnesses(current.negative_child, result)
        return result

    def all_illnesses(self):
        """
        The function finds all illnesses in the Tree & Their appearances
        :return: A sorted list of illnesses, from the most common illness to
        the least common illness in the Tree, each illness shown only once
        """
        final = self._find_all_illnesses(self.root, [])  # extract all leaves
        sorted_lst = sorted(final, key=lambda x: final.count(x), reverse=True)
        result = []
        for illness in sorted_lst:
            if illness not in result:
                result.append(illness)  # adds illnesses by common order
        return result

    def _paths_helper(self, illness, current, seq, result):
        """
        An helper function, finds all paths to reach illness given
        :param illness: The illness to reach in every path
        :param current: The current Node to check
        :param seq: A list of True / False represent each path
        :param result: The returned result list with all paths to illness
        :return: A list of lists, each inner list is a valid path to illness
        """
        if current.is_illness() and current.data == illness:
            result.append(seq[:])  # base case, found A valid path
            return
        if current.positive_child is not None:
            seq.append(True)
            self._paths_helper(illness, current.positive_child, seq, result)
            seq.pop()  # Backtrack to last option
        if current.negative_child is not None:
            seq.append(False)
            self._paths_helper(illness, current.negative_child, seq, result)
            seq.pop()  # Backtrack to last option
        return result

    def paths_to_illness(self, illness):
        """
        The function finds all paths to a specific illness
        :param illness: The current illness to reach it paths
        :return: A list of lists, each inner list represent a path to the
        illness given, True for Yes answer, False for No answer
        """
        if self.root.is_illness():
            return [[]]
        elif illness not in self.all_illnesses() and illness is not None:
            return []
        return self._paths_helper(illness, self.root, [], [])

    def _minimize_true(self, current_node):
        """
        The function Minimize all Nones data's from the Tree
        :param current_node: The current node we're checking
        :return: A root Node after minimization of all Nones in the Tree
        """
        if current_node.is_illness():
            return current_node
        first = self._minimize_true(current_node.positive_child)
        second = self._minimize_true(current_node.negative_child)
        if first.data is None and second.data is None:
            current_node.data = None  # remove's None data
            current_node.positive_child = None
            current_node.negative_child = None
            return current_node
        if first.data is None:
            current_node.data = second.data  # remove's None data
            current_node.positive_child = second.positive_child
            current_node.negative_child = second.negative_child
            return current_node
        if second.data is None:
            current_node.data = first.data  # remove's None data
            current_node.positive_child = first.positive_child
            current_node.negative_child = first.negative_child
            return current_node
        return current_node

    def _same_trees(self, pos, neg):
        """
        The function finds if both Trees are exactly the same or not
        :param pos: First Tree to check
        :param neg: Second Tree to check
        :return: True if identical, False otherwise
        """
        if pos is None and neg is None:
            return True
        if pos is not None and neg is not None:
            return ((pos.data == neg.data)
                    and self._same_trees(pos.positive_child,
                                         neg.positive_child)
                    and self._same_trees(pos.negative_child,
                                         neg.negative_child))
        return False

    def _minimize_false(self, current_node):
        """
        The function minimize all useless Nodes from the Tree
        :param current_node: The current Node object we're checking
        :return: A root node updated after removal useless Nodes
        """
        if current_node.is_illness():
            return current_node
        first = self._minimize_false(current_node.positive_child)
        second = self._minimize_false(current_node.negative_child)
        if self._same_trees(first, second):
            current_node.data = first.data  # found a useless Node object
            current_node.positive_child = first.positive_child
            current_node.negative_child = first.negative_child
            return current_node
        if not self._same_trees(first, second):
            return current_node

    def minimize(self, remove_empty=False):
        """
        The function minimize all useless Nodes according user choice
        :param remove_empty: False - remove all useless nodes,
        True - remove all useless nodes & all Nones data
        :return: An updated Diagnoser Tree object after the given removal
        """
        if remove_empty:
            self._minimize_true(self.root)
            self._minimize_false(self.root)
        elif not remove_empty:
            self._minimize_false(self.root)


def _build_helper(symptoms, depth, current_node):
    """
    The function creates A Tree of Nodes by symptoms given
    :param symptoms: The list of symptoms to ask in the Tree
    :param depth: The depth of each stage in our Tree
    :param current_node: The specific Node to place in the Tree
    :return: A root node contains the built Tree
    """
    if depth == len(symptoms) - 1:
        return Node(current_node)
    if depth < len(symptoms) - 1:
        return Node(current_node,
                    _build_helper(symptoms, depth + 1, symptoms[depth + 1]),
                    _build_helper(symptoms, depth + 1, symptoms[depth + 1]))


def _change_illness(root_node, illness, symptoms):
    """
    The function changes the leaves at the built Tree to the fitting illness
    :param root_node: The root node contains the Tree
    :param illness: The illness we need to place in A leaf Node
    :param symptoms: A symptoms list that fitting the current illness
    :return: None
    """
    if root_node.is_illness():
        root_node.data = illness  # changes leaf Node data to illness name
        return
    if root_node.data in symptoms:
        _change_illness(root_node.positive_child, illness, symptoms)
    if root_node.data not in symptoms:
        _change_illness(root_node.negative_child, illness, symptoms)
    return


def _check_valid_tree(records_lst, symptoms):
    """
    The function checks if current params are valid to built A Tree from
    :param records_lst: A Records object list
    :param symptoms: A list of string with all symptoms
    :return: True if can build A Tree with given params, False otherwise
    """
    for record in records_lst:
        if not isinstance(record, Record):
            raise TypeError('Your Record is not an Record object')
    for symptom in symptoms:
        if not isinstance(symptom, str):
            raise TypeError('Your symptom is not A str type')
    return True


def _dict_diagnoser(records_lst, all_symptoms, path):
    """
    The function finds The most common Record object that fits given path
    :param records_lst: The Records object lst
    :param all_symptoms: A list with all the symptoms in the Tree
    :param path: The specific path to check it most common illness that fits
    :return: A Records object that has the most appearances fitting path
    """
    illnesses_dict = {}
    for record in records_lst:
        if record.illness not in illnesses_dict.keys():
            illnesses_dict[record.illness] = 0  # creates Records dict
    for record in records_lst:
        if _record_fit_path(record, path, all_symptoms):
            illnesses_dict[record.illness] += 1
    max_count = max(illnesses_dict.values())
    if max_count != 0:
        for key in illnesses_dict.keys():
            if illnesses_dict[key] == max_count:
                return Record(key, path)  # most common key for those symptoms
    return None  # There is no illness fits the symptoms path given


def _all_symptoms_paths(current_node, seq, result):
    """
    The function finds all symptoms paths combination in the Tree
    :param current_node: The current Node object we're at
    :param seq: A list represent each path in the Tree
    :param result: The returned list contains all valid paths
    :return: A list with all symptoms paths in the Tree, all permutations
    """
    if current_node.is_illness():
        result.append(seq[:])  # found A valid path in the Tree
        return
    if current_node.positive_child is not None:
        seq.append(current_node.data)
        _all_symptoms_paths(current_node.positive_child, seq, result)
        seq.pop()
    if current_node.negative_child is not None:
        _all_symptoms_paths(current_node.negative_child, seq, result)
    return result


def _record_fit_path(record, path, all_symptoms):
    """
    The function finds if the given Record object fits the path
    :param record: The Record object
    :param path: The specific path to check
    :param all_symptoms: All symptoms in the Tree
    :return: True if the Record fits the path given, False otherwise
    """
    check_lst = []
    for symptom in all_symptoms:
        if symptom in record.symptoms:
            check_lst.append(symptom)
    if path == check_lst:
        return True  # fits the path
    return False


def _all_tree_symptoms(curr_node):
    """
    The function finds all the symptoms in the Tree
    :param curr_node: The root node of the Tree
    :return: A list with all symptoms in the Tree given
    """
    paths = _all_symptoms_paths(curr_node, [], [])
    result = []
    for path in paths:
        for elem in path:
            if elem not in result:
                result.append(elem)
    return result


def _new_records(paths, records_lst, all_symptoms_lst):
    """
    The function make a new Records list with only maximized Records objects
    :param paths: A list with all symptoms paths in the Tree
    :param records_lst: A list with all the Records objects
    :param all_symptoms_lst: A list with all the symptoms in the Tree
    :return: A new list of Records objects, only the most common by each path
    """
    result = []
    for path in paths:
        max_record = _dict_diagnoser(records_lst, all_symptoms_lst, path)
        result.append(max_record)
    return result


def _most_common_record(records):
    """
    The function finds which illness is the most common from all records
    :param records: A lst of Records objects
    :return: An illness with the most common appearances in the Records lst
    """
    res = {}
    for r in records:
        if r.illness not in res.keys():
            res[r.illness] = 0
    for r in records:
        res[r.illness] += 1
    max_appearances = max(res.values())
    for key in res.keys():
        if res[key] == max_appearances:
            return key


def build_tree(records, symptoms):
    """
    The function build a Tree according to given symptoms and Records objects
    :param records: A list of Records objects
    :param symptoms: A list of strings, represent the symptoms to ask for
    :return: A Diagnoser object, fitting the Tree that will be build
    """
    if _check_valid_tree(records, symptoms):
        if not symptoms and not records:
            return Diagnoser(Node(None))
        if not symptoms:
            for record in records:
                for r in record.symptoms:
                    if r not in symptoms:
                        symptoms.append(r)
            return Diagnoser(Node(_most_common_record(records)))
        built = Diagnoser(_build_helper(symptoms + [None], 0, symptoms[0]))
        if not records:
            return built
        paths = _all_symptoms_paths(built.root, [], [])
        all_symptoms = _all_tree_symptoms(built.root)
        new_records = _new_records(paths, records, all_symptoms)
        for record in new_records:
            if record is not None:
                _change_illness(built.root, record.illness, record.symptoms)
        return built  # returns the final Tree with fitting illnesses


def _check_valid_optimal(records, symptoms, depth):
    """
    The function finds whether given params are valid or not
    :param symptoms: A list with all symptoms
    :param depth: A int number of subsets in the Tree
    :param records: A list of Records objects
    :return: None if valid params, else raised fitting Exception error msg
    """
    if not 0 <= depth <= len(symptoms):
        raise ValueError('depth length is invalid')
    for symptom in symptoms:
        if symptoms.count(symptom) > 1:
            raise ValueError('found A duplicate symptom')
    for record in records:
        if not isinstance(record, Record):
            raise TypeError('found A non-Record type record')
    for elem in symptoms:
        if not isinstance(elem, str):
            raise TypeError('found A non-string type symptom')


def optimal_tree(records, symptoms, depth):
    """
    The function finds which Tree from all symptoms combinations got the
    largest success rate possible
    :param records: A list of Records objects
    :param symptoms: A list of all symptoms that will be subsets each Tree
    :param depth: The number of subsets symptoms
    :return: A Diagnoser object that has the largest success rate in the Tree
    """
    _check_valid_optimal(records, symptoms, depth)  # check validness params
    trees_dict = {}
    for symptoms_group in combinations(symptoms, depth):
        new_tree = build_tree(records, list(symptoms_group))
        trees_dict[new_tree] = new_tree.calculate_success_rate(records)
    max_rate = max(trees_dict.values())  # extract largest rate
    for key in trees_dict.keys():
        if trees_dict[key] == max_rate:
            return key  # optimal Tree will be returned
