List of Projects 
################
:date: 2018-11-14 22:06
:modified: 2018-11-14 22:08
:tags: list-of-projects
:category: All Projects
:slug: list-of-projects
:authors: Huawei Wang
:summary: Summary of projects


PhD Projects:
=============


- `Identification of Step Strategy Controller in Perturbed Walking <{filename}Projects/step-strategy-id.rst>`_

.. highlights::  

    .. figure:: /images/StepStrategy/StepStrategyIntro.png
        :width: 700px

    Step strategy (foot placement) controllers were identified from nine young adults’ walking data at three walking speed (0.8, 1.2, 1.6 m/s). Results showed that capture theory is not a bad estimation of how humans choose their foot placements, but a little bit conservative. In addition, identified control gains vary along with walking speed, which suggests that human choosing their foot placement does not based on a linear function of the feedback signals, but rather a nonlinear function.


- `Cycling Exoskeleton <{filename}Projects/virtual-cycling-Indego.rst>`_

    An Indego exoskeleton was used as a force feedback (haptic) device to provide corresponding resistance torques at hip & knee joints for users to do cycling. Dynamic parameters and friction model of the Indego was identified. Robust impedance control was used turned the Indego into a mass-spring-damper system and provided the virtual contact property. 


- `Identification of Joint Impedance Parameters in Perturbed Walking <{filename}Projects/walking-impedance-id.rst>`_

.. highlights::  

    .. figure:: /images/ImpedanceIdentification/ImpedanceIdIntro.png
        :width: 720px

    We are trying to show that a single perturbation at the treadmill belt speed is sufficient to identify parametric impedance controllers in all leg joints (hip, knee, and ankle). Simulated perturbed walking data is generating through a 2d gait model with the impedance control. Identification of the impedance parameters will be done on the generated simulation data.


- `Perturbed Walking Experiment <{filename}Projects/perturbed-walking-experiment.rst>`_

.. highlights::  

    .. figure:: /images/PerturbedWalkingExperiment/PerturbedWalking_APML.gif
        :width: 500px

    Collaborating with `Farzad Ehtemam <https://www.linkedin.com/in/farzad-ehtemam/>`_, 13 Gigabyte perturbed walking data of 21 young adults was collected. Perturbation signals were random speed changes which applied in both AP and ML directions. Recorded information includes kinematics (motion capture marker data), ground reaction force (2x6 dofs), and muscle activations (11 muscles in the right leg and torso).


- `Identification of Postural Controllers in Human Standing Balacne <{filename}Projects/standing-balance.rst>`_

    Standing balance experiment was conducted with random square wave perturbation. Multiple types controllers (linear and nonlinear) were identified from the experimental data. Identification results suggested that control system with cross joints feedback can better explain the experimental data. Nonlinear and time delay properties inside the control system helps explain testing participants' motion better also.

- `Bouncing Ball Optimization <{filename}Projects/ball-buncing-optimization.rst>`_ 

.. highlights:: 

    .. figure:: /images/BallBouncing/FinalResults.png
        :width: 600px 

    Converge speeds and results of multiple solvers in the IPOPT and SNOPT were examined through the bouncing ball trajectory optimization Problem. Bouncing ball system is the simplest system which has the similar strong nonlinear property as the human walk (landing). Results showed that IPOPT is more capable of solving this highly nonlinear problem than SNOPT. Different solvers inside IPOPT have roughly similar speed in solving the ball bouncing optimization. However, there are significant speed difference of different lengths of the trajectory optimization. 


**Master Projects:**
====================

- `Capture Theory Based on Modified LIP Models <{filename}Projects/capture-theory.rst>`_ 

.. highlights::  

    .. figure:: /images/CaptureTheory/CaptureTheoryWithCollision.png
        :width: 720px

    Capture theory is important not only for humanoid robot but also for amputees to adapt to more complex situation. This project calculated the capture point considering the existence of collision between ground and leg. Collision could reduce the velocity of CoM which is helpful for human to be captured. With the basic kinetics of Three-Dimensional Linear Inverted Pendulum Model (3D-LIPM), three collision models are proposed. Analytical equation of the capture points were calcualted with the collision models. Simulation results showed that smaller step length were generated with the collision models, which corherent with our hypothesis. 



