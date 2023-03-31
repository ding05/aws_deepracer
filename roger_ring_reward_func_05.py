def reward_function(params):

    # Example of rewarding the agent to follow center line

    # Read input parameters.
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_crashed = params['is_crashed']
    
    # Set the speed thresholds.
    speed_threshold_high = 1.0
    speed_threshold_low = 0.8

    # Calculate 3 markers that are at varying distances away from the center line.
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa.
    if distance_from_center <= marker_1:
        reward = 1.2
		# Give higher reward if the car runs faster and vice versa.
        if speed >= speed_threshold_high:
            reward += 1.0
        elif speed >= speed_threshold_low:
            reward += 0.5
        else:
            reward += 0
    elif distance_from_center <= marker_2:
        reward = 0.6
        if speed >= speed_threshold_low:
            reward += 0.3
    elif distance_from_center <= marker_3:
        reward = 0.02
    else:
        reward = 1e-3 # likely crashed / close to off track

    return float(reward)
