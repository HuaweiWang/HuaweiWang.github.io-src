.. _standing_balance:

Step controller identification in perturbed walking 
###################################################
:date: 2019-11-19 22:06
:modified: 2019-11-19 22:08
:tags: step-strategy-id
:category: Current Projects
:slug: step-strategy-id
:authors: Huawei Wang
:summary: Step controllers of nine test paricipants and three walking speeds were identified in the control strcture of the capture theory. Results suggested that the capture thoery is not a bad estimation of how human choose their foot location, but a little bit conservative. However, unlike the contant control gains for all walking speeds, control gains in identification results vary in different walking speeds.


Introduction
""""""""""""

Step strategy is essential for both human beings and humanoid robots to keep walking balance. Although many control algorithms has been proposed that can control humanoid robots to achieve stable walking under perturbation, there are limited studies that quantitively studied the control strategy of how humans choose their foot placement under perturbed environment. Identifying the human step controller itself is already an interesting topic. On the other hand, by understanding how humans take their steps, it is also helpful to improve the control of humanoid robotics and prosthetic/orthotic devices.

Capture theory has been developed more than a decade ago and is a successful step strategy for humanoid robots to keep walking balance. In this project, we are interested in knowing if the control structure of the capture theory can explain how humans choice their foot placement in walking, especially the perturbed walking.

Method
""""""

We identified step controllers from randomly perturbed walking data with a nonlinear gait model through the indirect identification approach. The identified step controllers have the same feedback structure as the capture theory, but their feedback gains were identified from perturbed walking data. Perturbed walking data was recorded by previous study, in which perturbation is continuously random belt speed changes. The nonlinear gait model is a two dimensional seven-link dynamic model which has been used in many human walking studies. The indirect identification approach guarantees that the identified step controller is able to drive the nonlinear gait model as a closed-loop system generating the expecting motion. The diagram plot of the indirect identification approach in this paper is shown below. The general idea of it is to optimize the control parameters inside the locomotion controller to minimize the difference between the joint motion of the simulation model and the experimental data.  

    .. figure:: /images/StepStrategy/IdentificationStructure.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center



Result
""""""

Identification results show that human beings use relatively close but smaller feedback gains to find the foot placement comparing to the capture theory. Center of mass (CoM) position and velocity are sufficient as feedback signals to have a good foot placement estimation, however, the feedback control is more likely to be a nonlinear function, rather than the linear function suggested by the capture theory. 

Identified CoM postion and velocity gains are shown below. Comparing to the capture theory (grey lines), test participants use relative smaller gains in almost all the three waling speeds.


    .. figure:: /images/StepStrategy/Gains.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

With identified step controllers, the swing leg is controlled to follow the swing path which was generated based on the estimated desire foot location. Since perturbation exists, the desire foot location is not a constant postion at ground, but changing with the CoM states. This plot shows the estimated foot locaiton and swing path changes in one swing period.

    .. figure:: /images/StepStrategy/Walking_Motion.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

Onging Work
"""""""""""

Next step of this project is to apply the identified (average) step controller on the Indego exoskeleton. The goal is to test whether the identified step controller can help choose good foot placement in perturbed walking.  

Healthy participants will wear the Indego exoskeleton and walking on the treadmill with belt speed perturbation. Legs of the Indego will be controlled by identified step controller during the swing phase. In stance phase, Indego legs will be passive. EMG sensors will be placed on participants to record their muscle activations. Our hypothsis is that participants' leg muscule activiations in swing phase will be smaller than wearing all passive Indego. 

To achieve this goal, we have embeded the ground reaction force (GRF) signal from our instrumented treadmill into Indego control system, which will be used as swing/stance phase detector. Here is a video demo shown that the instrumented treadmill is connected with Indego and can control it's motion. 


.. youtube:: MKcbGxQCNR8
    :class: youtube-4x3
    :allowfullscreen: no
    :seamless: no



