def controller(enow, epast):
    # Implement a simple proportional-derivative (PD) controller
    Kp = 0.15  # Proportional gain
    Kd = 0.6  # Derivative gain

    # Calculate the control action
    action = Kp * enow + Kd * (enow - epast)
    
    return action