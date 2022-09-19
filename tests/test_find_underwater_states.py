from src.sealevel_rise import find_underwater_states
import numpy as np

def test_non_edge_connected_states():
    '''test that states where the land elevation is lower than sea level, but 
    aren't actually connected to the sea are not classed as underwater'''

    input = np.array([[0,0,0,0,0,0],
                      [0,0,1,1,0,0],
                      [0,0,1,1,0,0],
                      [0,0,0,0,0,0]])
    
    expected_output = np.array([[0,0,0,0,0,0],
                                [0,0,0,0,0,0],
                                [0,0,0,0,0,0],
                                [0,0,0,0,0,0]])

    actual_output = find_underwater_states(input)

    np.testing.assert_array_equal(expected_output,actual_output)

