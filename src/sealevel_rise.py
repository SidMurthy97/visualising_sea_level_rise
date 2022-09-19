import numpy as np
import matplotlib.pyplot as plt



def apply_sea_level(sealevel: int, topography: np.ndarray) -> np.ndarray:
    '''function returns coordinates that would be below the sea level as 1
    and anything above as 0'''
    
    #simple thresholding
    boolean_topography = topography < sealevel

    return boolean_topography

def find_underwater_states(thresholded_topography: np.ndarray) -> np.ndarray:
    '''Function performs connected components analysis to find the different 
    bodies in the topography. It then analyses whether the body is connected to
    the border. It returns an array of land elevations normalised to the set 
    sea level.'''
    x_size,y_size = thresholded_topography.shape

    #pad the array to represent connection to the sea
    connected_topography = np.pad(np.zeros([x_size,y_size]),[(1,1),(1,1)],mode='constant',constant_values=10)
    
    blob_count = 0
    total_neighbours = 9
    neighbors_checked = 0
    error_count = 0
    sea_connection = 0
    #iterate through the thresholded topography and populate the connected one
    neighbouring_indices = [-1,0,1]
    for i in range(x_size):
        for j in range(y_size):
            neighbors_checked = 0
            error_count = 0

            #offset indices on the connected topograhy
            x,y = i + 1, j + 1
            if thresholded_topography[i,j] == True:
                
                
                #if state is underwater, check neigbours
                for dx in neighbouring_indices:
                    for dy in neighbouring_indices:
                        #TODO:raise index error exception is a negative index is being tried
                        try:
                            #if neighbour is already assigned a blob, assign 
                            #current state to the same blob

                            if connected_topography[x + dx,y + dy] > 0:
                                connected_topography[x,y] = \
                                    connected_topography[x + dx,y + dy]    
                            else:
                                #increment counter recording 
                                neighbors_checked += 1

                        # #catch exceptions to do with index errors 
                        except IndexError as e:
                            error_count += 1
                        
            #if no neighbours were found
            if neighbors_checked + error_count == total_neighbours:
                blob_count += 1
                connected_topography[x,y] = blob_count
            # print(neighbors_checked,error_count,total_neighbours)
    
    #iterate through the topography again to resolve conflicts, and remove any
    #states not connected to the edges
    for i in range(x_size):
        for j in range(y_size):
            #again offset the indices
            x, y = i + 1, j + 1

            if connected_topography[x,y] != 0:
                sea_connection = 0
                #check if any neighbours = padded value
                try:
                    for dx in neighbouring_indices:
                        for dy in neighbouring_indices:
                            if connected_topography[x+dx,y+dy] == 10:
                                sea_connection += 1
                except IndexError as e:
                    continue

                connected_topography[x,y] = 10 if sea_connection > 0 else 0
    
    # connected_topography = connected_topography.astype(bool)

    #return the non-padded connected topography
    return connected_topography[1:-1,1:-1].astype(bool)