include "pnu_robot.lua"

TRAJECTORY_BUILDER.pure_localization = true
POSE_GRAPH.optimize_every_n_nodes = 20

MAP_BUILDER.num_background_threads = 6
POSE_GRAPH.constraint_builder.sampling_ratio = 0.5 * POSE_GRAPH.constraint_builder.sampling_ratio
POSE_GRAPH.global_sampling_ratio = 0.1 * POSE_GRAPH.global_sampling_ratio
POSE_GRAPH.max_num_final_iterations = 1

return options

