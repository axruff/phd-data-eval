# Data evaluation scripts for benchmarking of optical flow methods on X-ray data

Used in PhD thesis: "Automated Analysis of Time-resolved X-ray Data using Optical Flow Methods"

[Full text (pdf)](https://github.com/axruff/PhD-Thesis/blob/master/PhD_Thesis_Ershov.pdf)

[Full text on Karlsruhe Institute of Technology Library](https://publikationen.bibliothek.kit.edu/1000055519)



Benchmarking approach follows the procedure described in:


[A Database and Evaluation Methodology for Optical Flow](http://vision.middlebury.edu/flow/floweval-ijcv2011.pdf)

[Middlebury Vision Database](http://vision.middlebury.edu/flow/)



## Example: Image noise

![alt text](https://github.com/axruff/phd-data-eval/blob/master/screenshots/exp_noise_hyd.png "Nose Modelling")

Figure: Modeling noise for the *Hydrangea* dataset using the *Gaussian* noise model.
(a) First frame of the original image sequence. (b) Image with added Gaussian noise
with standard deviation *sigma* = 20. (c) Image with added Gaussian noise with standard
deviation *sigma* = 40. Bottom Row: Corresponding histograms. Note a dramatic change in
the grey value distribution as a result of noise.

![alt text](https://github.com/axruff/phd-data-eval/blob/master/screenshots/exp_noise_hyd_res.png "Evaluation results")

Figure: Evaluation of optical flow performance on noisy data with *Gaussian noise*.
For all datasets an average *endpoint error* (AEE) is shown in 3 regions: *All* region is
depicted as a green plot; *Untext* region as a blue plot and *Disc* region as a red plot.
Left: *RubberWhale* dataset. Middle: *Hydrangea* dataset. Right: *New Marble* dataset.
Method: *Baseline* optical flow algorithm

## Example: Models comparison on degraded data

![alt text](https://github.com/axruff/phd-data-eval/blob/master/screenshots/exp_models.png "Models comparison")

Figure: Comparison of optical flow models M1 - M7 on the *RubberWhale* dataset
with added noise and image artifacts. (a) First frame of degraded image sequence. (b)
Second frame of the sequence. (c) Ground truth result. (d) Model M1: Classical Horn
and Schunck. (e) Model M2 = M1 + flow-driven smoothness term. (f) Model M3 = M2 + multi-level computation. (g) Model M5 = M4 + robust data term + combined localglobal approach. (h) Model M7 = M5 + median filtering + data refinement step.


