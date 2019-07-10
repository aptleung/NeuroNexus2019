# NeuroNexus2019

This project is our solution to a Brain Segmentation problem presented by NeuroNexus 2019. Traditional techniques to segment a brain MRI
used probablities to assign a pixel as grey matter, white matter, CSF, dura, or skull. It oftens fails to identify any anomalies and requires
doctors to manually edit these, taking away valuable time. 
<br/><br/>
Our team designed a solution by training a Convolutional Neural Network (CNN) to take 23x23 patches surrounding each pixel of an MRI scan
and classify that pixel based on its surroundings. Included here are the steps to read in, normalize, and process an MRI image along with
the CNN model's training and testing. 
