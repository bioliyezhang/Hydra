# -*- coding: cp936 -*-
"""
Usage: hydra.py -p parameter_file.txt
-p parameter file				*[No default value]
"""


if __name__ == "__main__":
## Import modules
    import matplotlib
    matplotlib.use('Agg')
    import sys
    import hydra.pipeline
    PIPELINE = hydra.pipeline
    import hydra.helper
    HELPER = hydra.helper

    list_args = sys.argv[1:]

    if '-h' in list_args:
        print __doc__
        sys.exit(0)
    elif len(list_args) < 2 or '-p' not in list_args:
        print __doc__
        sys.exit(0)
    else:
        param, parameter_file, updates = HELPER.update_parameters(list_args)


    #if we resume we specify the old parameter file
    HELPER.initialize_standard(param)
    HELPER.write_updated_file(updates, param, parameter_file)

    HELPER.initialize_qsub(param)
    HELPER.read_fastq_filenames(param)
    HELPER.initialize_logfiles(param)

    HELPER.writeLog('Initializing all module parameters ... \n', param)
    PIPELINE.initialize_all(param)

    HELPER.writeLog('Initializing successful!\n', param)
    HELPER.writeLog('####################################################\n', param)

## run pipeline
    HELPER.writeLog('Running all modules: \n\n', param)
    PIPELINE.run_all(param)

## reporting
    HELPER.report_start(param)
    PIPELINE.report_all(param)
    HELPER.report_finish(param)




