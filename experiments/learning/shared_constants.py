import numpy as np
AGGR_PHY_STEPS = 100
FREQ = 100
NUM_DRONES = 2
ENV = 'payloadcoop'


# For PayloadCoop
PHYSICS = 'pyb'
DRONE_MODEL = 'cf2x'
OBS = 'payload_one_sensor'
ACT = 'xyz_yaw'
SENSOR_MODE = 1 # 0: sensor points in absolute frame, 1: sensor points in body frame
DEST_POINT = np.array([0, 10, 0.5])
MAX_DISTANCE_BETWEEN_DRONE = 1.0
INIT_RADIUS = MAX_DISTANCE_BETWEEN_DRONE / 5
EPISODE_LEN_SEC = 45.0
STATE_TOL = 1.05 # Tolerance of state value against maximum state constant
IS_ARRIVE_POS_TOL = 0.15
IS_ARRIVE_VEL_TOL = 0.25
MAX_XY = 15.0
MAX_Z = 3.0
K_MOVE = 5
MAX_SENSOR_DIST = 2.0
MAX_SENSOR_ANGLE = 10.0
# Randomization Obstacle
# 0 < RadiusInit = MAX_DISTANCE_BETWEEN_DRONE/4 < MIN_DIST_FROM_ORIGIN < obstacle_position < MAX_DIST_FROM_ORIGIN < DEST_POINT
MAX_DIST_FROM_ORIGIN = 4
MIN_DIST_FROM_ORIGIN = 2


# Reward
RWD_HIT = -1e3
RWD_TOOFAR_DRONE = -1e2
RWD_ARRIVE = 5e3
RWD_OUTOFFIELD = -1e2
RWD_DIST_DEST = -10 / FREQ * AGGR_PHY_STEPS
RWD_DIST_BETW_DRONE = -1 / FREQ * AGGR_PHY_STEPS
RWD_TIME = -0 / FREQ * AGGR_PHY_STEPS
RWD_RPM = -1e-6/ FREQ * AGGR_PHY_STEPS
RWD_DIST_Z = 0 / FREQ * AGGR_PHY_STEPS

# Training
LR = 5e-5
GAMMA = 0.99
N_STEP = 5



# assert 0 <= MAX_DISTANCE_BETWEEN_DRONE / 4 <= MIN_DIST_FROM_ORIGIN <= MAX_DIST_FROM_ORIGIN <= np.linalg.norm(DEST_POINT), "Error MIN/MAX_DIST_FROM_ORIGIN"

