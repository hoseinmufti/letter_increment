BEGINNING_LETTER = 'A'
ENDING_LETTER = 'Z'

class LetterIncrement():
    def increment_sequence(self, input_sequence:str, incrementation_range=1) -> list:
        """
        Increments a sequence of letters.\n
        returns a list of incremented letter sequences according to range provided
        """
        # Assign beginning and ending letter
        if input_sequence.isupper():
            beginning_letter = BEGINNING_LETTER
            ending_letter = ENDING_LETTER
        elif input_sequence.islower():
            beginning_letter = BEGINNING_LETTER.lower()
            ending_letter = ENDING_LETTER.lower()
        else:
            raise ValueError("""Sequence fails to contain same case.\n
                             Please provide either a sequence of complete uppercases or a sequence of complete lowercases.""")

        # Assign letters sequence
        sequence = input_sequence
        # Convert sequence into list
        sequence_list = list(sequence)
        # Assign sequence len
        sequence_len = len(sequence) 

        # Assign sequences to list
        sequences = []

        # increment sequence according to range provided
        for _ in range(incrementation_range): 
            # iterrate over each letter in sequence
            for i, letter in enumerate(reversed(sequence_list), start=1):
                # If not 'Z', increment the selected letter and assign in sequence list
                if letter != ending_letter:
                    incremented_letter = chr(ord(letter) + 1)
                    sequence_list[-i] = incremented_letter
                    break
                # Else if 'Z',
                else:
                    # Change current letter to 'A'
                    if i <= sequence_len:
                        new_letter = beginning_letter
                        sequence_list[-i] = new_letter

                    # And if reached last letter, add 'A' to root, and update sequence len so next itteration itterates over new root
                    if i == sequence_len:
                        sequence_list = [beginning_letter] + sequence_list
                        sequence_len = len(sequence_list)

            # Print incremented sequence
            incremented_sequence = ('').join(sequence_list)
            sequences.append(incremented_sequence)

        return sequences