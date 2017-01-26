
# 比赛状态
CONTEST_STATUS = {
    'PENDING': 0,
    'RUNNING': 1,
    'ENDED': 2,
}


# 判题状态
JUDGE_STATUS = (
    (-1, 'Reserved'),
    (0, 'Accept'),
    (1, 'Presentation Error'),
    (2, 'Wrong Answer'),
    (3, 'Time Limit Exceed'),
    (4, 'Memory Limit Exceed'),
    (5, 'Output Limit Exceed'),
    (6, 'Run Time Error'),
    (7, 'Compile Error'),
    (8, 'Pending'),
    (9, 'Pending Rejudge'),
    (10, 'Compiling'),
    (11, 'Rejudging'),
)
