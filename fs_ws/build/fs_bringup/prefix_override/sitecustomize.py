import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kiran_gunathilaka/development/mlcv/cone_detection_navigation/fs_ws/install/fs_bringup'
