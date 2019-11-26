Capture Theory Based on Modified LIP Models
###########################################
:date: 2019-11-19 22:06
:modified: 2019-11-19 22:08
:tags: capture-theory
:category: All Projects
:slug: capture-theory
:authors: Huawei Wang
:status: draft
:summary: Capture theory based on modified LIP models


Introduction
""""""""""""
Push recovery ability has been received much attention in recent years because it is
essential for biped robot to work in non-lab environment. This ability could prevent
biped robot from falling down when facing some perturbations or even big collision.

Even though capture theory based on the 3D-LIPM has a relatively complete and
inspiring result, it is conservative because of strict hypothesis. For example, the collision between swing leg and ground was not considered. in this paper, we primarily interested in the influence of capture point calculating if the
collision is taken into consideration. Three ideal collision models are proposed here to represent the heel-strike
process, which still makes the euqation of capture theory in a analytical format.


Method
""""""

Collision model 1
'''''''''''''''''
The hypotheses of collision model 1 are as follow, and the change of velocities before
and after collision is shown in the plot.

[1] The velocities of CoM before and after collision only exist in the horizontal plane.

[2] The collision is ideal and happens instantaneously.

[3] During collision and after the legs shifting, the length of trailing leg keeps constant.

    .. figure:: /images/CaptureTheory/collsion_model1.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center


According to the hypotheses and velocities changes before and after collision, the
instantaneous capture point of this model is calculating as follow:


    .. figure:: /images/CaptureTheory/capture_equation1.png
        :width: 700px
        :align: center
        :alt: alternate text
        :figclass: align-center



Collision model 2
'''''''''''''''''
The hypotheses of collision model 2 are as follow, and the change of velocities before
and after collision is shown in the plot.

[1] The velocities of CoM before and after collision only exist in the horizontal plane.

[2] The collision is ideal and happens instantaneously.

[3] During collision, both the leading leg and trailing leg keep in constant length L (Lis the length of original leg).

[4] After the collision, the velocity of mass is vertical to the leading leg.

    .. figure:: /images/CaptureTheory/collsion_model2.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

According to the hypotheses and velocities changes before and after collision, the
instantaneous capture point of this model is calculating as follow:

    .. figure:: /images/CaptureTheory/capture_equation2.png
        :width: 700px
        :align: center
        :alt: alternate text
        :figclass: align-center


Collision model 3
'''''''''''''''''
The hypotheses of collision model 3 are as follow, and the change of velocities before
and after collision is shown in the plot.

[1] The velocities of mass before and after collision only exist in the horizontal plane.

[2] The collision is ideal and happens instantaneously.

[3] During collision, the mass is still kept in the same horizontal plane.

[4] During collision, both the leading leg and trailing leg keep in the same constant length.

[5] During the collision, the velocity of mass is vertical to the leading leg.

    .. figure:: /images/CaptureTheory/collsion_model3.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

According to the hypotheses and velocities changes before and after collision, the
instantaneous capture point of this model is calculating as follow:

    .. figure:: /images/CaptureTheory/capture_equation3.png
        :width: 700px
        :align: center
        :alt: alternate text
        :figclass: align-center

Result
""""""

Instantaneous capture point results are compared in the following plot. X-axis represents velocity of CoM and Y-axis represents the distance
between instantaneous capture point and the location of CoM. Red line is the result of
3D-LIPM without collision. Green line is the result of 3D-LIPM with collision model
1. Blue line is the result of 3D-LIPM with collision model 2. Pink line is the result of
3D-LIPM with collision model 3. The result of 3D-LIPM without collision is linear,
which means that the instantaneous capture point will go to infinite distance along
with the increase of CoM velocity. However, with the increase of velocity of CoM,
the results of 3D-LIPM with collision models approach to a constant value. This
means that, collision is helpful for human to get into capture state. A preliminary
human push recovery test also indicates that the collision is useful, especially when
under large pushes (high CoM velocity).

    .. figure:: /images/CaptureTheory/comparison_of_estimated_step_length.png
        :width: 500px
        :align: center
        :alt: alternate text
        :figclass: align-center

Related Reports and Publications
""""""""""""""""""""""""""""""""

**[1]** `Calculation of Capture Point Considering the Existence of Collision. <{static}/pdfs/CapturePointWithCollision.pdf>`_




