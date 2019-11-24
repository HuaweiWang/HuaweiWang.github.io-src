Virtual Cycling Machine using Indego
####################################
:date: 2019-11-19 22:06
:modified: 2019-11-19 22:08
:tags: virtual-cycling-Indego
:category: projects
:slug: virtual-cycling-Indego
:authors: Huawei Wang
:status: draft
:summary: Impedance controller identification in human walking unber perturbation


Introduction
""""""""""""

Human motion is caused by internal and external forces. Internal forces are the muscle forces generated inside human bodies. External forces are the forces externally applied on human bodies, for instance, ground reaction forces, Gravity, contact forces. Internal forces affect motion through the human muscle-skeleton system. External forces affect motion through skeleton system. In the identification studies, control parameters of different human motions (standing balance and walking) were identified by reproducing the same motion with muscle-skeleton models and external environment (ground).  
 

However, external forces (torques) can also be applied directly to the human joints, which could have the same affect of external environment. For instance, leg exskeleton can apply appropriate resistance torques at hip and knee joints to generate the similar (same) effect of cycling activity. In this project, the Indego exskeleton is used to applied the required resistance torques. In other words, we are going to trun the Indego into a cycling machine.

Method
""""""

First part of this project is simulation work, in which a human body model, exskeleton model, and a cycling dynamic model are created. And their connection is shown in the following figure.

    .. figure:: /images/VirtualCycling/Principles.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

More detail of this part of work can be found in the `Wiki
<https://github.com/HuaweiWang/Virtual-Cycling-Simulator/wiki>`_ of the Virtual Cycling Simulator GitHub repository.

The exoskeleton model was built based on the identified model parameters of the Indego. This model was used in the simulation test of the robust impedance controller that applied on Indego hardware. Identified parameters include segment inertia, center of mass and motion frictions. segment weight and length were mannually measured.

Annimation of the forward simulation of this simulation system is shown below:


    .. figure:: /images/VirtualCycling/optimize3_result_annimation.gif
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center


Result
""""""



Discussion
""""""""""


