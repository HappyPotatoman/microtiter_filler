import unittest
from plate_filler import PlateFiller, PlateFillError

class TestPlateFiller(unittest.TestCase):
    def setUp(self):
        self.plate_filler = PlateFiller(plate_size = 96,
                                        samples = [['Sam 1']],
                                        reagents= [['Reag X']],
                                        replicas= [1],
                                        number_of_plates= 1)

    def test_validate_plate_size_with_non_integer(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_plate_size("96")
        self.assertEqual(str(context.exception), "Invalid plate size input. Expected an integer, but got <class 'str'>.")

    def test_validate_plate_size_with_invalid_integer(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_plate_size(100)
        self.assertEqual(str(context.exception), "Invalid plate size 100. Expected 96 or 384.")

    def test_validate_samples_with_non_list(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_samples("string")
        self.assertEqual(str(context.exception), "Samples should be a list of lists of strings.")
    
    def test_validate_samples_with_non_nested_list(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_samples(["string"])
        self.assertEqual(str(context.exception), "Each element of samples should be a list of strings.")
    
    def test_validate_reagents_with_non_list(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_reagents("string")
        self.assertEqual(str(context.exception), "Reagents should be a list of lists of strings.")
    
    def test_validate_reagents_with_non_nested_list(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_reagents(["string"])
        self.assertEqual(str(context.exception), "Each element of reagents should be a list of strings.")
    
    def test_validate_replicas_with_non_list(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_replicas("string")
        self.assertEqual(str(context.exception), "Replicas should be a list of integers.")
    
    def test_validate_replicas_with_non_integer(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_replicas(["string"])
        self.assertEqual(str(context.exception), "Expected a integer replica, but got <class 'str'> instead.")

    def test_validate_number_of_plates_with_non_integer(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_number_of_plates("string")
        self.assertEqual(str(context.exception), "Invalid number of plates input. Expected an integer, but got <class 'str'>.")
    
    def test_validate_number_of_plates_is_negative_integer(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_number_of_plates(-1)
        self.assertEqual(str(context.exception), "Number of plates has to be a non-negative integer, but got -1.")
    
    def test_validate_number_of_experiments_with_mismatched_lengths(self):
        with self.assertRaises(ValueError) as context:
            self.plate_filler.validate_number_of_experiments([["sample1"]], [["reagent1"]], [1, 2])
        self.assertEqual(str(context.exception), "Number of experiments is not consistent length of samples: 1, length of reagents: 1, length of replicas: 2.")

    def test_get_plate_dimensions_for_96(self):
        self.plate_filler.plate_size = 96
        num_rows, num_cols = self.plate_filler.get_plate_dimensions()
        self.assertEqual(num_rows, 8)
        self.assertEqual(num_cols, 12)
    
    def test_get_plate_dimensions_for_384(self):
        self.plate_filler.plate_size = 384
        num_rows, num_cols = self.plate_filler.get_plate_dimensions()
        self.assertEqual(num_rows, 16)
        self.assertEqual(num_cols, 24)
    
    def test_check_if_enough_plates_sufficient_wells(self):
        self.plate_filler.plate_size = 96
        self.plate_filler.number_of_plates = 1
        self.plate_filler.samples = [['sample1', 'sample2']]
        self.plate_filler.reagents = [['reagent1', 'reagent2']]
        self.plate_filler.replicas = [1]
        
    def test_check_if_enough_plates_insufficient_wells(self):
        self.plate_filler.plate_size = 96
        self.plate_filler.number_of_plates = 1
        self.plate_filler.samples = [['sample1', 'sample2', 'sample3']]
        self.plate_filler.reagents = [['reagent1', 'reagent2', 'reagent3']]
        self.plate_filler.replicas = [12]
        with self.assertRaises(PlateFillError):
            self.plate_filler.check_if_enough_plates()

if __name__ == '__main__':
    unittest.main()
