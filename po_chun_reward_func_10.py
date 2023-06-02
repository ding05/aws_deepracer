def reward_function(params):

    # Read input parameters.
    speed = params['speed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_crashed = params['is_crashed']
    abs_steering = abs(params['steering_angle'])
    
    # Set up the speed reward.
    speed_reward = 0.0
    if speed > 1.05:
        speed_reward = 1.2
    elif speed > 1.03:
        speed_reward = 1.0
    elif speed > 1.0:
        speed_reward = 0.7
    elif speed > 0.97:
        speed_reward = 0.5
    elif speed > 0.95:
        speed_reward = 0.3
    elif speed > 0.93:
        speed_reward = 0.1
    else:
        speed_reward = 0.0001
    
    # Set up the distance reward.
    # Set up the markers that are at varying distances away from the center line.
    marker_1 = 0.15 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.5 * track_width
    distance_reward = 0.0
    if distance_from_center <= marker_1:
        distance_reward = 1.0
    elif distance_from_center <= marker_2:
        distance_reward = 0.3
    elif distance_from_center <= marker_3:
        distance_reward = 0.01
    else:
        distance_reward = 0.0001
        #if is_crashed == True:
            #distance_reward -= 1.0
    
    # Sum the rewards.
    reward = speed_reward + distance_reward
    
    # Penalize if car steers too much to prevent zigzag.
    abs_steering_threshold = 20.0
    if abs_steering > abs_steering_threshold:
        reward *= 0.8

    return float(reward)