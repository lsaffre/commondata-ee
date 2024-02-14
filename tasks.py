from atelier.invlib import setup_from_tasks

ns = setup_from_tasks(globals(),
                      "commondata.ee",
                      revision_control_system='git')
