import random
import string

class Configs:

    def __init__(self) -> None:
        pass

    def random_id_generator(self):
        """
        This function generates a unique UUID for the mandatory PubNum API parameter and returns a string.
        """

        alphabet_string = string.ascii_letters
        alphabet_list = list(alphabet_string)

        num_string = string.digits
        num_list = list(num_string)

        combined_lst = alphabet_list + num_list

        part_1 = ''.join(random.choice(combined_lst) for i in range(8))

        return part_1

