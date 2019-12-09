Virtual Cycling Machine using Indego
####################################
:date: 2019-11-19 22:06
:modified: 2019-11-19 22:08
:tags: virtual-cycling-Indego
:category: All Projects
:slug: virtual-cycling-Indego
:authors: Huawei Wang
:status: draft
:summary: Impedance controller identification in human walking unber perturbation


Introduction
""""""""""""

Human motion is caused by internal and external forces. Internal forces are the muscle forces generated inside human bodies. External forces are the forces externally applied on human bodies, for instance, ground reaction forces, gravity, and contact forces. Internal forces affect motion through the human muscle-skeleton system. External forces affect motion through skeleton system.  

However, external forces (torques) can also be applied directly to the human joints, which could have similar affects of external environment. For instance, leg exskeleton can apply appropriate resistance torques at hip and knee joints to generate the similar effect of cycling activity. In this project, the Indego exskeleton is used to applied the required resistance torques. In other words, we are trunning the Indego exoskeleton into a cycling machine.

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


Annimation of the forward simulation of this simulation system is shown below. Pink arcs are the joint torque that human need to provided to drive the virtual circling system. Horizental and virtual vectors are the virtual contact force between the Indego's end-effectors and virutal pedals.   


    .. figure:: /images/VirtualCycling/optimize3_result_annimation.gif
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center


The Indego exoskeleton model was built based on the identified model parameters of the Indego.  Identified parameters include segment inertia, center of mass and motion frictions. segment weight and length were mannually measured. This model was used to design the robust impedance controller that represent the contact model between Indego's end-effector and the pedal of the virutal crankset system.


Curently ongoing work focus on the hardware control tests and human involved experiments.




