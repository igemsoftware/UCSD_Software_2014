import sbider_searcher as search
import sbider_grapher as graph
import unittest
import sbider_database as db
import sbider_parser as parse
import sbider_searcher as search
import helper

class sbider_unit(unittest.TestCase):
    def test_fail_parser(self):
        """testing faulty query."""
        conn, cur = db.db_open("sbider.db")
        try:
            self.logic = parse.parse_logic(cur, "A and B = C")
        except TypeError:
            pass
        db.db_close(conn,cur)
    
    def test_successful_parser(self):
        """testing a successful query of the sbider network"""
        conn, cur = db.db_open("sbider.db")
        self.logic = parse.parse_logic(cur, "lara and arac = gfp")
        self.assertEquals(type(self.logic), dict)
        db.db_close(conn,cur)

    def test_searcher_direct(self):
        """testing the following query lara and arac to gfp for the direct traverse"""
        conn, cur = db.db_open("sbider.db")
        user_query =  "lara and arac = gfp"
        logic_dictionary = parse.parse_logic(cur, user_query)
        input_dictionary, output_dictionary = db.make_ope_id_spe_id_dics(cur)
        repressor_dictionary = db.make_ope_id_rep_spe_id_dic(cur)
        self.operon_path_list = search.get_sbider_path(input_dictionary,repressor_dictionary,\
                                                    output_dictionary, ['2', '38'], ['11'], False)

        for operon_path in self.operon_path_list:
            current_species = ['2', '38']
            for operon in operon_path:
                self.assertEquals(current_species in input_dictionary[operon], True)
                current_species = output_dictionary[operon][0]
        db.db_close(conn,cur)
        
    def test_searcher_direct_2(self):
        """testing the following query tetr and arac = yfp for the direct traverse"""
        conn, cur = db.db_open("sbider.db")
        user_query =  "tetr and arac = yfp"
        logic_dictionary = parse.parse_logic(cur, user_query)
        input_dictionary, output_dictionary = db.make_ope_id_spe_id_dics(cur)
        repressor_dictionary = db.make_ope_id_rep_spe_id_dic(cur)
        self.operon_path_list = search.get_sbider_path(input_dictionary,
										  repressor_dictionary,
										  output_dictionary,
										  ['8', '12'],
										  ['37'],
										  False)
        for operon_path in self.operon_path_list:
            current_species = ['12', '8']
            for operon in operon_path:
                self.assertEquals(current_species in input_dictionary[operon], True)
                current_species = output_dictionary[operon][0]
        db.db_close(conn,cur)

    def test_searcher_indirect(self):
        """testing the following query tetr and arac = gfp for the indirect traverse"""
        conn, cur = db.db_open("sbider.db")
        user_query =  "arac and lara = gfp"
        logic_dictionary = parse.parse_logic(cur, user_query)
        input_dictionary, output_dictionary = db.make_ope_id_spe_id_dics(cur)
        repressor_dictionary = db.make_ope_id_rep_spe_id_dic(cur)
        self.operon_path_list = search.get_sbider_path(input_dictionary,
                                                           repressor_dictionary,
                                                           output_dictionary,
                                                           ['2', '38'],
                                                           ['11'],
                                                           True)
                                                           
        for operon_path in self.operon_path_list:
            current_species = ['2', '38']
            input_species_set = set(current_species)
            output_species_set = set(current_species)
            for operon in operon_path:
                input_species = helper.uniquely_merge_list_of_lists(input_dictionary[operon])
                output_species = helper.uniquely_merge_list_of_lists(output_dictionary[operon])
                for species in input_species:
                    if species in output_species_set:
                        input_species_set.add(species)
                for species in output_species:
                    output_species_set.add(species)
            self.assertEquals(input_species_set.issubset(output_species_set), True)
        db.db_close(conn,cur)

    def test_searcher_indirect_2(self):
        """testing the following query ahl and laci = gfp for the indirect traverse"""
        conn, cur = db.db_open("sbider.db")
        user_query =  "ahl and laci = gfp"
        logic_dictionary = parse.parse_logic(cur, user_query)
        input_dictionary, output_dictionary = db.make_ope_id_spe_id_dics(cur)
        repressor_dictionary = db.make_ope_id_rep_spe_id_dic(cur)
        self.operon_path_list = search.get_sbider_path(input_dictionary,
                                                       repressor_dictionary,
                                                       output_dictionary,
                                                       ['13', '22'],
                                                       ['11'],
                                                       True)
                
        for operon_path in self.operon_path_list:
            current_species = ['13', '22']
            input_species_set = set(current_species)
            output_species_set = set(current_species)
            for operon in operon_path:
                input_species = helper.uniquely_merge_list_of_lists(input_dictionary[operon])
                output_species = helper.uniquely_merge_list_of_lists(output_dictionary[operon])
                for species in input_species:
                    if species in output_species_set:
                        input_species_set.add(species)
                for species in output_species:
                    output_species_set.add(species)
                self.assertEquals(input_species_set.issubset(output_species_set), True)
        db.db_close(conn,cur)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
