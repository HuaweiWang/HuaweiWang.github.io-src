.. _standing_balance:

Step controller identification in perturbed walking 
###################################################
:date: 2019-11-19 22:06
:modified: 2019-11-19 22:08
:tags: step-strategy-id
:category: Current Projects
:slug: step-strategy-id
:authors: Huawei Wang
:summary: Step controller identification in human walking under perturbation


Introduction
""""""""""""

Step strategy is essential for both human beings and humanoid robots to keep walking balance. Although the capture theory has been developed as a successful step strategy for humanoid robots to keep walking balance under unpredictable environment, we are curious if the human beings use the same control algorithm to choose their foot placements.

We are interested in knowing if the step controller that has the same feedback structure as the capture theory can be got by learning how humans choice their foot placement in walking, especially the perturbed walking. This not only can help us understand how good the capture theory is in explaining humans’ choice, but also may able to help improve its capability in balanced walking. 

Method
""""""

We identified step controllers from randomly perturbed walking data with a nonlinear gait model through the indirect identification approach. The identified step controllers have the same feedback structure as the capture theory, but their feedback gains were identified from perturbed walking data. Perturbed walking data was recorded by previous study, in which perturbation is continuously random belt speed changes. The nonlinear gait model is a two dimensional seven-link dynamic model which has been used in many human walking studies. The indirect identification approach guarantees that the identified step controller is able to drive the nonlinear gait model as a closed-loop system generating the expecting motion. The diagram plot of the indirect identification approach in this paper is showing in Figure 1. The general idea of it is to optimize the control parameters inside the locomotion controller to minimize the difference between the joint motion of the simulation model and the experimental data. Identification results show that human beings use relatively close but smaller feedback gains to find the foot placement comparing to the capture theory. Center of mass (CoM) position and velocity are sufficient as feedback signals to have a good foot placement estimation, however, the feedback control is more likely to be a nonlinear function, rather than the linear function suggested by the capture theory.  

    .. figure:: /images/StepStrategy/IdentificationStructure.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center



Result
""""""

Twenty-five out of twenty-seven identification problems were identified successfully.

Gains
    .. figure:: /images/StepStrategy/Gains.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

Motions

    .. figure:: /images/StepStrategy/Walking_Motion.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

Discussion
""""""""""

In this study, step controllers that have the same feedback structure as the capture theory were successfully identified from walking experiment data. Identification results suggested that the capture point is not a bad estimation but a little bit conservative in explaining humans’ step choice. In addition, human choosing their foot placement does not based on a linear function of the feedback signals, but rather a nonlinear function.


