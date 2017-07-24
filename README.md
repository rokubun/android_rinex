Android GNSS Logger to RINEX converter
======================================


This repository contains a Python script that converts logs from Google's GNSS
measurement tools to RINEX

The repository for the GNSS measurement Android app can be found in this link:

https://github.com/google/gps-measurement-tools

Once installed in your Android device, the app will log GNSS measurements
and will write a text file with the GNSS measurements. There is a file in
the `data` folder that contains an example data file collected with a Nexus 9
tablet:

    data/pseudoranges_log_2017_07_17_13_46_25.txt

This file can be used with this tool to generate a RINEX file that can be
then used in GNSS data processing software such as e.g. RTKLib.

Examples
--------

The script has a small help that explains the different options of the 
program. This help is accessed through the command:

    android_to_rinex.py -h

There are several options that allow the user to change several standard
RINEX fields ('MARKER NAME', 'RECEIVER TYPE', ...)

Some execution examples follow:

(a) Process the data file and generate a RINEX file in the standard output 
    (discard the error messages)

    android_to_rinex.py data/pseudoranges_log_2017_07_17_13_46_25.txt 2> /dev/null

(b) Process the data and save the results into a specified file name (and 
    disregard warning messages)

    android_to_rinex.py -o nex91980.17o data/pseudoranges_log_2017_07_17_13_46_25.txt 2> /dev/null

(b) Process the data, trying to "integerize" the observations to the nearest
    time stamp (i.e. integerize the time stamp to the closest second and
    modify the pseudorange uaing the PseudoRangeRateMeterPerSecond measurements=.
    Note: this option does not touch the carrier phase. In theory the same could
    be done to the phase, but strictly speaking we would need the Doppler. not
    the PseudoRangeRate measurements.

    android_to_rinex.py -i -o nex91980.17o data/pseudoranges_log_2017_07_17_13_46_25.txt 2> /dev/null

    This option might be useful to process data from various smartphones at 
    once.

(d) Process the data and generate a named RINEX data but maintaining 
    constant the 'FullBiasNanos' instead of using the instantaneous value.
    This avoids the 256 ns jumps each 3 seconds that create a code-phase
    divergence due to the clock.

    android_to_rinex.py -b -o nex91980.17o data/pseudoranges_log_2017_07_17_13_46_25.txt 2> /dev/null



