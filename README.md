# DFTS_compat_v1
Deep Feature Transmission Simulator (DFTS) which runs in tensorflow.compat.v1

Originally released in 2018 [[1]](#references), DFTS was developed to be compatible with Tensorflow version 1 (more specifically, version 1.12) and Keras 2.2.2. The demo paper [[2]](#references) gave a brief overview of the simulator. Various changes in Tensorflow 2 [[3]](#references) break the operation of DFTS. The Tensorflow 1.12 code from DFTS can be run with little modification in Tensorflow 2 by disabling the v2 behavior. This repository contains DFTS code modified to run in Tensorflow 2.2.0 (no Keras needed) in Tensorflow v1 compatibility mode. Furthermore, this repository contains scripts to run classification simulations in DFTS.

## DFTS_TF2 
A fully Tensorflow v2 compatible DFTS is now available at [[4]](#references)! I strongly recommend to use this new TF2-compatible version of DFTS. 

## Contents
To be completed.

## Overview
To be completed.


## References
### [1] Unnibhavi, H. (2018) DFTS (Version 1.0) [[repo](https://github.com/SFU-Multimedia-Lab/DFTS)]

### [2] H. Unnibhavi, H. Choi, S. R. Alvar, and I. V. Bajić, "DFTS: Deep Feature Transmission Simulator," demo paper at IEEE MMSP'18, Vancouver, BC, Aug. 2018. [[pdf](https://www.researchgate.net/publication/327477545_DFTS_Deep_Feature_Transmission_Simulator)]  

### [3] Effective TensorFlow 2 [[guide](https://www.tensorflow.org/guide/effective_tf2)]

### [4] Dhondea, A. (2020) DFTS_TF2 (Version 1.0) [[repo](https://github.com/AshivDhondea/DFTS_TF2)]

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/AshivDhondea/DFTS_compat_v1/blob/master/LICENSE) file for details
