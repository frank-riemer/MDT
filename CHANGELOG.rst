*********
Changelog
*********

v1.2.1 (2020-02-14)
===================

Changed
-------
- Small fix to the buffer allocation flags. The post-processing failed sometimes.


v1.2.0 (2020-02-14)
===================
Upgrade to match the latest version of MOT, which contains a vast number of changes regarding buffer and kernel allocation.


v1.1.5 (2020-01-25)
===================

Added
-----
- Adds CL load balancing option to the model processing functions.

Changed
-------
- Updates the credits with sponsors information.
- Renamed extra_prior to prior in the compartment and composite model definitions.

Other
-----
- Following changes in MOT to allow easier cl environment initialization.


v1.1.4 (2019-12-17)
===================

Added
-----
- Adds some introduction text to the mdt.conf file.

Other
-----
- Small bugfix in the noddi-dti computation. MD was changed in place.


v1.1.3 (2019-12-17)
===================
- Upped the voxel batch size again as the previous change did not provide a solution.


v1.1.2 (2019-12-17)
===================

Changed
-------
- Changed the default optimization batch size from 100k to 10k voxels per run. Due to changes in MOT, the current batch size fails for some users.

Changed
-------
- Removed the NODDI-DTI maps from the Tensor and KurtosisTensor post-processing. They do not seem to be widely used.
  For users that do desire these maps there are two ways to go about it:

  1) Reinstate the post-processing. This can be done by going to the
  Tensor compartment model, and add ``noddi_dti_maps`` to the
  extra_optimization_maps list. This function can be imported from:
  ``from mdt.lib.post_processing import noddi_dti_maps``.

  2) Use the function mdt.compute_noddi_dti() to compute the maps manually
  based on optimization results. Typically used as:

  .. code-block:: python

      results = mdt.fit_model(model, input_data, ...)
      noddi_dti = mdt.compute_noddi_dti(model, input_data, results)


v1.1.1 (2019-12-16)
===================

Added
-----
- Adds infrastructure to be able to represent the gradient vector as spherical angles in a compute kernel.
- Added weight sum to one transformation to the FIM objective function.

Changed
-------
- Removed local reduction from the Tensor-DTI post-processing. This was unnecessary.
- Moved all the input data classes and functions to a dedicated module.
- Renamed get_parameter_codec to get_mle_codec.

Other
-----
- Followed changes in MOT allowing the work to be better splitted over workitems.
- Moved repository to private github account.


v1.1.0 (2019-12-06)
===================

Added
-----
- Adds optimization and runtime options to the get_optimization_inits function.
- Adds wild and residual bootstrapping functionality.
- Adds a post-processing flag to the model to disable computation of the log likelihood and the information criterion maps.
- Adds a separate compute_fim function to MDT. This can be used to compute the FIM matrix post-hoc.
- Adds the IVIM model.
- Adds the poisson distributed ActiveAx model, courtesy by Mark Drakesmith from CUBRIC.

Changed
-------
- Changed some of the parameter transformations.
- Changed signature of the input data copy_with_updates function.

Other
-----
- From the composite model, removed the voxels_to_analyze context. Instead, we now use the 'get_subset' method from the kernel data objects. This allows for cleaner code.
- Removed a few more mot_float_types for either float or double.
- Implements the meta-parameters 'observations', 'observation_ind' and 'nmr_observations' in the compartment model.
- Removed Numpy future warning concerning stacking using generators.


v1.0.0 (2019-06-04)
===================
Version 1.0 marking the end of the PhD of MDT's lead developer Robbert Harms.
This software package will still be supported for the foreseeable future by Robbert.
Future development will continue by CBCLab, Maastricht University under the supervision of Alard Roebroeck.
For ideas, please check the "Development Ideas" page.

As a personal note to all the users of MDT. Thank you all for using MDT and for your invaluable feedback over the past years. I could not have done it without you.

Best wishes, Robbert


v0.21.0 (2019-04-01)
====================
This version marks the complete removal of the Cascade models.

MDT still does cascaded initialization by default, but now using predefined initializations.
The automatic initialization can of course be disabled and or overwritten using manual provided data. See the manual for instructions.

There are two reasons for this change. First, the default cascade was used in 99% of the cases. Removing it and making it an implicit default simplifies the code.
Second, the code change provides an opportunity of future extensions towards multi-modal modeling.

Added
-----
- Added base class for EstimableModels.

Fixed
-----
- Fixed bug in handling the gradient deviations.

Removed
-------
- Removed the Cascade models.

Other
-----
- Slight restructuring of the modules.


v0.20.3 (2019-03-08)
====================

Changed
-------
- Reverted the parameter transformation of the weights back to the CosSqrClamp parameter transformation. This proves superior in edge cases.

Other
-----
- Fixed spelling mistake in GUI (misspelled Brain as Brian).


v0.20.2 (2019-02-26)
====================

Other
-----
- Bug fix in the create_covariance_matrix, it sometimes tried to get the shape attribute of a dictionary, crashing the computations. This only happened in rare occasions.


v0.20.1 (2019-02-21)
====================

Other
-----
- Removed atomic function from the KurtosisTensor, it was redundant.


v0.20.0 (2019-02-19)
====================
This version is the first version to support arbitrary non-linear inequality constraints.
Currently, during optimization, these constraints are enforced using the penalty method (https://en.wikipedia.org/wiki/Penalty_method).

Added
-----
- Adds special parameter classes for the spherical parameters. Now, the composite model will take care of the necessary transformations to keep the spherical parameters theta and phi within the right spherical hemisphere.
- Adds support for inequality constraints to the compartments and composite models.
- Adds utility function for merging dictionaries in inheriting component templates.

Changed
-------
- Changed parameter transformation of the weights from CosSqrClamp to ScaleTransform

Removed
-------
- Removed the post-optimization modifiers. They were unnecessary since capability of specifying constraints.

Other
-----
- Added files for docker/singularity intel builds


v0.19.1 (2019-01-08)
====================
- Corrected MOT version requirements.


v0.19.0 (2019-01-08)
====================
The primary change in this version is that we now use the pseudo-inverse for computing the covariance matrix from the Hessian.
This is as good as a direct inverse but faster to compute and more robust to voxels with a badly conditioned Hessian.

Added
-----
- Adds support for masked colors setting in the maps visualizer.

Changed
-------
- Changed Fisher Information Matrix computation to use an eigen-decomposition based pseudo-inverse for all voxels.
- Changed the signature of the batch_apply function to have the path as first argument. The subject info of the batch functions now include the data folder as property.

Fixed
-----
- Fixed small issue in the GUI where shells were not correctly counted and represented due to a sorting issue in the protocol class.


v0.18.4 (2018-12-11)
====================

Changed
-------
- Improved the Hessian computation of the models after fitting.
- Changed the default BinghamNODDI_r1 initialization to depend on the Watson NODDI model.


v0.18.3 (2018-12-05)
====================

Changed
-------
- Adds model_names option to the run_function_on_batch_fit_output batch function.
- Removed some numpy warnings in the qMT model.
- Increased the JohnsonNoise eta upper bound.


v0.18.2 (2018-12-02)
====================

Changed
-------
- Changed the maximum bounds to real numbers, anticipating bounded optimization methods. It used to be -inf and +inf, it is now -1e20 and 1e20.
- The initialization dictionary now also recognizes MDT models with a suffix. Like "BinghamNODDI_r1_MySuffix", which will load the initialization from "BinghamNODDI_r1".


v0.18.1 (2018-11-23)
====================

Added
-----
- Adds the ``use_cascaded_inits`` flag to the model fit command to simplify the new initialization interface.
- Adds reduced Ramani QMT models to MDT.

Other
-----
- Made the generate_wm_mask function more general.
- Made all mot_float_type4 vectors float4 and moved some other parts from mot_float_type to either float or double depending on the situation.
- Removed the building pattern from the composite models.


v0.18.0 (2018-11-19)
====================
This version marks the deprecation of the Cascade models in MDT.
Instead, MDT now strikes a balance between customizability and ease of use.
For ease of use, using the GUI and command line MDT now automatically selects a good starting point based on pre-set rules.
For customizability you can use the Python API in which you first compute the initialization point and then manually provide it to the model fitting.
By providing it manually you can have a finer grained control over the initialization settings.

For more details on how to properly initialize in newer newer versions see :ref:`model_fitting`.
Even though this functionality is now deprecated, it will still be available for the near future to allow users the chance to move to the new workflow.

Changed
-------
- Deprecated the Cascade interface in favor of a more direct control of the initialization point.
- Refactored the documentation and added sampling documentation.


v0.17.2 (2018-11-14)
====================

Changed
-------
- Changed the specification of the volume selection in the composite models to allow selection based on all protocol columns.

Other
-----
- Small update to the BallStick cascade inits to make sure they are within bounds.
- Small update to the weight numerical differentiation to not use the upper bound anymore. Provides for slightly better uncertainty computations.


v0.17.1 (2018-11-12)
====================

Changed
-------
- Updated the Kurtosis initial parameter positions to try to prevent out of bounds problems within the optimization routines.


v0.17.0 (2018-11-09)
====================
The way the boundary constraints of the parameters are enforced is changed.
Previously MDT used parameter transformations to enforce boundary conditions, in this new version we use the new support of MOT for the boundary conditions.
In the new MOT version, boundary conditions (box-constraints) are handled by returning INFINITY if the bound is violated.
While this is a crude way of enforcing boundary conditions, it does relieve us of the parameter transformations in MDT.

As a result, fits looks slightly less noisy overall, and it seems to fit better in relaxometry models.


Added
-----
- Adds additional parameters types to link the likelihood functions better with the models.
- Adds support for the special parameter '@noise_std' to inject the current noise standard deviation into a compartment model.

Changed
-------
- Changed the way the bounds are handed in the optimization.
- Changed the likelihood function to always include the constant terms.

Fixed
-----
- Fixed bug in the mdt-estimate-noise-std method.

Other
-----
- Small update to the GDRCylinder bounds.
- Following the support in MOT for boundary constraints, changed the parameter transformations of the parameters.
- Small fix to the batch profiles, it did not pick up the noise_std.txt files.
- Documentation updates.
- Small update to the mdt-math-img command. Better way of handling multiple outputs.


v0.16.4 (2018-10-30)
====================

Changed
-------
- Changed the volume selection syntax to allow defining multiple ranges.

Other
-----
- Slight refactoring of the NonParametricTensor compartment, removing the strict bounds.


v0.16.3 (2018-10-30)
====================

Fixed
-----
- Fixed documentation building.


v0.16.2 (2018-10-30)
====================

Changed
-------
- Corrected, in the post-processing of composite models, the sort order for Python <3.6 versions.


v0.16.1 (2018-10-29)
====================

Changed
-------
- Changed the map sorting feature in the post-processing of composite models. The new specification is easier to follow and more general.

Other
-----
- Following changes in MOT.


v0.16.0 (2018-10-26)
====================
All implemented models are now also compatible with POCL (tested with POCL version 1.1).

Changed
-------
- Moved the memory allocation of the computation caching to the KernelData.


v0.15.8 (2018-10-24)
====================
Most of the models are now compatible with POCL (tested with POCL version 1.1).
Only the models with a cache will not work with POCL yet (BinghamNODDI, Ball&Racket, AxCaliber).


Other
-----
- Following changes in MOT
- Removed some local variable instances


v0.15.7 (2018-10-19)
====================
Fixed an important bug in the code that was present since version 0.14.8. The noise std was not correctly set anymore in the log likelihood method.
All users are advised to upgrade to this version.

Fixed
-----
- Fixed the issue that the noise std was not set correctly due to naming issues in the log likelihood function.


v0.15.6 (2018-10-17)
====================

Changed
-------
- Updated the rotate orthogonal vector CL function. This reverts changes from a few versions ago, this gives the same value but faster and more stable.
- Work on moving local variable declarations outside of non-kernel functions. This should in the future allow running MOT on LLVM OpenCL implementations. More work needed.

Other
-----
- Speed-up of Tensor post-processing.
- Refactoring of the NODDI model.
- Removed the AxonDensity index from the AxCaliber models.


v0.15.5 (2018-10-09)
====================

Fixed
-----
- Fixes the issue that the models would not load.


v0.15.4 (2018-10-08)
====================

Fixed
-----
- Fixed the init user settings initialization for newer versions of Python.

Other
-----
- Following changes in MOT (changed the function signature of the Legendre Polynomial).


v0.15.3 (2018-10-06)
====================

Other
-----
- Update requirement to newer MOT version to fix NODDI computation overflow.


v0.15.2 (2018-10-05)
====================
- Small fix to make AxCaliber working again.


v0.15.1 (2018-10-04)
====================
- Small update to the ActiveAx and NODDI models. Reordering the compartments provides a slightly better fit in some voxels.


v0.15.0 (2018-10-04)
====================
The most important change in this version is the new caching feature for compartment models.
This cache is meant to contain values that are constant per volume, to speed up the evaluation of the compartment model for each volume.
The speed-up is dependent on the model, but for AxCaliber and Bingham NODDI the speed-up is about 2~5x.

Added
-----
- Adds a caching mechanism for caching computations in a compartment model.
- Added a post-sampling callback to add additional results to the sampling output.
- Adds average auto correlation to the sampling post processing.
- Adds default RWM epsilons for the SCAM MCMC algorithm, set to 1e-5 times the initial proposal standard deviation of a parameter.

Other
-----
- Use nifti.header instead of nifti.get_header() when working with Nibabel.


v0.14.13 (2018-09-16)
=====================

Changed
-------
- Updated the AxCaliber model to provide only the basic AxCaliber. People can edit the basic model for their own purposes.


v0.14.12 (2018-09-15)
=====================

Added
-----
- Adds the AxCaliber model


v0.14.11 (2018-09-12)
=====================

Added
-----
- Adds Watson NODDI ExVivo model.
- Adds Bingham NODDI with two directions.


v0.14.10 (2018-09-11)
=====================
- Renamed the Bingham normalization function to the Confluent Hypergeometric function.
- Small refactoring of the NODDI model (model is still the same).


v0.14.9 (2018-09-10)
====================

Added
-----
- Adds the Bingham NODDI model.
- Adds theta/phi to vector to the sampling post processing.
- Adds univariate normal fits to the sampling post-processing.

Other
-----
- Refactored the descriptions of the components
- Removed (object) declaration from the class declaratoins, it is no longer needed with Python 3.


v0.14.8 (2018-08-29)
====================

Added
-----
- Adds the VERDICT model, according to Panagiotaki 2014, Noninvasive Quantification of Solid Tumor Microstructure Using VERDICT MRI.
- Adds the Van Gelderen physical diffusion models for spherical diffusion.


v0.14.7 (2018-08-29)
====================

Added
-----
- Adds the Neuman physical diffusion models for spherical diffusion.


v0.14.6 (2018-08-28)
====================

Added
-----
- Adds AstroSticks and AstroCylinders compartment models.
- Adds Ball&Rackets model.


v0.14.5 (2018-08-24)
====================

Added
-----
- Adds support for weighted objective function computations during model fitting and sampling.


v0.14.4 (2018-08-24)
====================

Added
-----
- Adds the NODDI-DTI kappa and odi conversion.

Other
-----
- Support for complex numbers in model functions using PyOpenCL.


v0.14.3 (2018-08-23)
====================
This version is significantly faster than previous versions when run using a GPU. All users are recommended to update
to this version.

Other
-----
- Following changes in MOT.
- Small cosmetic improvement in the C code.


v0.14.2 (2018-08-17)
====================

Added
-----
- Adds NODDIDA.
- Adds method argument to the mdt sample function.

Other
-----
- Removed redundant super arguments.
- Refactorings following changes in MOT.


v0.14.1 (2018-08-02)
====================
- Removed some non-ascii characters for compatibility.


v0.14.0 (2018-08-02)
====================
- Following changes in MOT, in particular how the optimization routines are called.


v0.13.5 (2018-07-17)
====================

Changed
-------
- Updated makefile to use twine for uploading to PyPi.
- Replaced Grako for Tatsu, as Grako was no longer supported.
- Removed the Tatsu debian package and added it as a Pip requirement.
- Removed six as compatibility layer.


v0.13.4 (2018-07-16)
====================

Added
-----
- Adds documentation on debugging OpenCL elements.
- Adds a button to the maps visualizer to only show the set options in the textual frame.
- Adds simple data compression to the gradient deviation computations in the case of zeros off the diagonal.
- Added the covariance terms to the error propagation of Tensor FA.

Changed
-------
- Changed method signature of saving view map plots.
- Small update to the unweighted volume computation in the Protocol, it now multiplies the gradient vector with the diffusivities to account for non-normalized gradients.


v0.13.3 (2018-07-01)
====================
A small maintenance release for cleaning up some unused or outdated features.

Changed
-------
- Removed the used_protocol.prtcl from the output folder. Since with the extra_protocol the input has become more convoluted, the used protocol no longer reflects the actual used inputs.
- Removed the cascade_subdir from the model fit arguments. This behaviour was easily replicated by providing another output directory.
- Removed the save_user_script_info from the fit model parameters. It was hardly used and not a primary function of MDT.
- Renamed the post-processing switch covariance to covariances and added the switch for variances. Both must be set to False to disable computation of the FIM. If only one of them is False, the FIM will be computed and only the elements desired will be returned.


v0.13.2 (2018-07-01)
====================

Added
-----
- Adds support for gradient deviations per volume.
- Adds spherical proposal transformations to the theta and phi parameters. This ensures valid proposals around the [0, pi] range for both theta and phi.

Changed
-------
- Simplified the implementation of the NODDI_IC compartment model by removing support for cylindrical diffusion.
  This simplifies the requirements of the model by removing the need to supply 'delta', 'Delta' and 'G'.
  NODDI results are unaltered since the cylindrical diffusion was not used anyway.

Other
-----
- Removed the (previously) deprecated static map parameters.
- Renamed the DMRICompositeModelTemplate to CompositeModelTemplate.
- Removed some deprecated attributes from the compartment models.


v0.13.1 (2018-06-04)
====================

Fixed
-----
- Fixed small issue found by Dr. Luke Edwards. The legendre polynomial in the NODDI_IC compartment was not computed correctly. This only subtly changes the results.


v0.13.0 (2018-06-01)
====================
This version removes support for Python version <= 2.7. Now only Python > 3 is supported.

Added
-----
- Adds the CHARMED_r1 model using the van Gelderen model of diffusion.
- Adds scientific articles section to the docs.
- Adds Ubuntu 18.04 release target.
- Adds a convenience function for generating a brain mask.

Changed
-------
- Updates default protocol save name.
- Removed Python2.7 support.

Other
-----
- Mac compatibility change.
- Slightly changed the masking algorithms with a different median filter.


v0.12.1 (2018-05-15)
====================

Fixed
-----
- Fixes issue with the JohnsonNoise model in the model builder.

Other
-----
- Renamed some of the command line commands from generate to create.


v0.12.0 (2018-05-03)
====================
The most important update is a bugfix in the CHARMED models. Unfortunately the CHARMED reference paper (Assaf, 2004) contains
a small omission in the formula for the Neuman cylindrical diffusion model (a ``2`` is missing).
Correcting this mistake slightly changes the CHARMED results.

Furthermore, the static maps and static parameters have been merged with the protocol parameters.
This allows, or will allow in the future, overloading protocol parameters with 3d/4d volumes.

Added
-----
- Added functionality for nesting templates. This allows adding components that can only be used in the context of another component.
- Adds EPI relaxometry models.
- Adds functionality for unique names in a cascade.
- Adds the Van Gelderen cylinder model and renamed the Von Neumann cylinder model. Corrected the CHARMEDRestricted equation.

Other
-----
- Redefined the kappa parameter of the NODDI model to be between 0 and 64.
- Removed the static map parameters and merged these with the protocol parameters.
- Merged the model builder with the composite model.


v0.11.4 (2018-04-12)
====================

Fixed
-----
- Fixed a bug which made the mdt-model-fit no longer work.


v0.11.3 (2018-04-11)
====================

Changed
-------
- Updates to the docs.
- Following changes in MOT.


v0.11.2 (2018-04-09)
====================

Fixed
-----
- Fixed small regression in mdt-batch-fit.

Other
-----
- Moved the model building modules from MOT to here.


v0.11.1 (2018-04-04)
====================

Changed
-------
- Updated the MOT version requirements.


v0.11.0 (2018-04-04)
====================
This version contains a completely new (backwards compatible) component loading mechanism.
Templates now add themselves to a library module, such that you can define models and components everywhere, and have MDT use it automatically.
Furthermore, components can now overwrite existing components, and you can reuse previously defined component templates.
As an example of defining a new model in your script:

.. code-block:: python

    import mdt

    class NewModel(mdt.CompositeModelTemplate):
        ...

    mdt.fit_model('NewModel', ...)


Here, we are defining a new composite model ``NewModel`` using the ``CompositeModelTemplate``.
Due to using this template, the model is automatically added to the MDT library.
It is also possible to overwrite existing models, as for example:

.. code-block:: python

    import mdt

    class Tensor(mdt.components.get_template('composite_models', 'Tensor')):
        likelihood_function = 'Rician'

    mdt.fit_model('Tensor (Cascade)', ...)


Here, we are loading the current definition of the ``Tensor`` composite model and overwrite it with an updated likelihood function.
Overwriting, since we name this class Tensor again.
The updated Tensor model will now be used everywhere, also in cascade models that use that Tensor.

To remove an entry, you can use, for example:

.. code-block:: python

    mdt.components.remove_last_entry('composite_models', 'Tensor')


See the section :ref:`components_defining_components` for more details on this modeling.


Added
-----
- Adds S0-T2 cascade model.
- New module loading mechanism that allows loading models from everywhere.
- Template mechanism for the batch profiles.

Changed
-------
- Updated the documentation to follow the new model loading mechanism.
- By default, now runs Powell with a patience 5 for the S0-T2 model (updated the config).
- Renamed dependency_list to dependencies in the models and library functions.
- Renamed parameter_list to parameters in the compartment models and in the library functions.

Fixed
-----
- Adds hole filling to the mask generation.
- Fixed delayed brain mask logging info in the GUI.

Other
-----
- Following changes in the MOT samplers.
- Renamed DMRICompositeModelTemplate to CompositeModelTemplate.
- Renamed Maastricht to Microstructure (Diffusion Toolbox).
- Removed noise component loader items.


v0.10.9 (2018-02-22)
====================

Added
-----
- Adds covariance singularity boolean matrix to the output results.

Fixed
-----
- Fixed small bug in the mdt maps visualizer. Refactored the batch fitting function to use the batch apply function.


v0.10.8 (2018-02-16)
====================

Changed
-------
- Updated the map view config syntax for the voxel highlights (now called annotations).
- Updates following MOT in DKI measures.
- Changed the config layout of the maps visualizer with regards to the colorbar settings.


v0.10.7 (2018-02-14)
====================

Changed
-------
- Changed the parameter proposal and transform function of the PHI parameter.

Fixed
-----
- Fixes issue #4, the MDT gui crashed on startup with Qt version 5.9.1.


v0.10.6 (2018-01-30)
====================

Added
-----
- Adds colormap order in the GUI when a map is interpreted as colormap.
- Adds relaxometry models.
- Adds sampling output selection to the sampler.
- Adds another post-processing switch to the sampling post-processing.
- Adds nibabel and numpy array decoration to store path info alongside the niftis when loaded with mdt.load_nifti().
- Adds Hessian and covariance computation as post-processing to the models.

Changed
-------
- Updates to the batch profiles.
- Updates to CHARMED boundary conditions.

Other
-----
- Removed the sampling statistics calculation from the post-processing, it did not work out theoretically.
- Adds an utility function for computing the correlations from the covariances.
- Small update to the scientific scrollers in the gui. Interchanged the position of max and min in the gui.
- Renamed evaluation_model to likelihood_function in the composite models. This covers the usage better.


v0.10.5 (2017-09-22)
====================

Added
-----
- Adds support for multiple output files in the mdt-math-img CLI function.
- Adds post sampling log messages
- Adds caching to deferred loading collections.

Changed
-------
- Changed the signature of write_nifti and moved the header argument to the optional keyword arguments.
- Updates to the documentation of the configuration.
- Small improvements in the post-sampling processing.
- the function ``write_nifti`` now creates the directories if they do not exist yet.

Fixed
-----
- Fixed non working documentation build on read the docs. Removed the ``sphinxarg.ext`` since it is not supported yet on read the docs.

Other
-----
- Small path updates to the batch profiles.
- MDT now also saves the log likelihood and log priors after sampling.
- Made the sampler sample from the complete log likelihood. This allows storing the likelihood and prior values and use them later for maximum posterior and maximum likelihood calculations.
- Simplified model compartment expressions due to improvements in MOT.


v0.10.4 (2017-09-06)
====================

Changed
-------
- Changes the default sampling settings of the phi parameter. Since it is supposed to wrap around 2*pi, we can not use the circular gaussian approximation if we are constraining it between 0 and pi, instead we use a simple gaussian proposal and a truncated gaussian sampling estimate.
- Updates to the processing strategies. Adds an interface for MRIModels to work with the processing strategies.

Other
-----
- Following the changes in MOT, we can now let a compartment model and a library function evaluate itself given some input data.


v0.10.3 (2017-08-29)
====================

Added
-----
- Adds some of the new config switches in the maps visualizer to the graphical interface.
- Adds the possibility of interpreting vector maps as RGB maps. Useful for displaying Tensor FA orientation maps.
- Added overridden method to the problem data.
- Adds support for fitting when the protocol is empty.
- Added parameter name logging to MDT instead of in MOT.

Changed
-------
- Updated the processing strategy with a better mask file placement (technical thing).
- Updates to the sampling post-processing.
- Updates to the documentation.
- Updated the InputDataMRI interface to contain a few more properties.
- Updated the changelog generation slightly.
- Updated the ExpT1DecIR model, adds a cascade. Updated the way cascades are updated as such that it allows for multiple copies of the same model in a cascade.
- Updates to the GUI.
- Updates the parser to the latest version of Grako.

Fixed
-----
- Fixed naming issues when loading new maps in the map viewer.
- Fixes the image squeezing in the viewer when adding a colorbar.
- Fixed the issue with the get_free_param_names removal.

Other
-----
- Version bump.
- Small refactoring in the processing strategy.
- Renamed the S0-TIGre model to S0_TI_GRE.
- Reverted some changes on the S0-T1-GRE model.
- Renamed InputDataMRI to MRIInputData and InputDataDMRI to SimpleMRIInputData.
- Renamed 'problem_data' to 'input_data', 'DMRIProblemData' to 'InputDataDMRI' and all other possible renamings. This also deprecates the function  since it has been renamed to .
- Following changes in MOT.


v0.10.2 (2017-08-23)
====================

Added
-----
- Adds chunk indices look-a-head in the processing strategies. This allows the Processor to start pre-loading the next batch.


v0.10.1 (2017-08-22)
====================

Changed
-------
- Updates to the GUI.
- Updates to the maps visualizer.


v0.10.0 (2017-08-17)
====================

Added
-----
- Adds automatic changelog generation from the git log.
- Adds multivariate statistic to sampling output. Changes the KurtosisExtension to a KurtosisTensor single model.
- Adds catch for special case.
- Adds Tensor reorientation as a post processing. This reorients theta, phi and psi to match the sorted eigen vectors / eigen values.
- Adds compartment model sorting based on weights as a post-processing to composite models. Adds automatic sorting to Ball&Sticks and CHARMED models.
- Adds small boundary conditions to the Kurtosis model.
- Adds clickable point information to the map visualization GUI.
- Adds name collision resolution in the visualization GUI after dragging in images with the same name.
- Adds a library function for the kurtosis matrix multiplication.
- Added component construction to the __new__ of a component template. This allows the template to construct itself at object initialization.

Changed
-------
- Changes the way the logging is condensed during optimization.
- Updates to the GUI.
- Updates to the documentation. Also, the compartment models now no longer need their own files, they can be defined in any file in the compartment_models directory.
- Updates to the documentation, renamed the Kurtosis compartment to KurtosisExtension and made it require the Tensor in the Composite model.
- Updates to the documentation. Updates to the Kurtosis model. Sets boundary conditions correct and adds post-processing.
- Updates to the documentation style.

Fixed
-----
- Fixed bug in matplotlib renderer with the highlight voxel.
- Fixed the small GUI bug with the random maps naming.

Other
-----
- Removed calculated example files.
- Removed redundant logging.
- Small renaming updates.
- Adds some linear algebra methods to the utilities, Changed the way the psi component of the Tensor is used.
- More work on the post-sampling statistics.
- Removed redundant model.
- Moved more relaxometry compartments to the single python file. Slightly increased the number of voxels in sampling.
- Update to the cartesian to spherical function.
- First work on map sorting.
- Small bugfix in the MRI constants.
- Small function reshuffling, updates to comments.
- Small fix with the InitializationData in the fit model.
- Small bugfix to the GUI.
- Completely adds the Kurtosis model. Adds some small library functions as well for the Tensor and Kurtosis computations.


v0.9.40 (2017-07-27)
====================

Added
-----
- Adds ActiveAx cascade.

Other
-----
- Small release to add ActiveAx cascade model.
- Small update to docs.


v0.9.39 (2017-07-26)
====================

Changed
-------
- Updates to the documentation

Other
-----
- Small fix allowing b-value to be stored in protocol alongside Delta, delta and G.
- Removed the functionality of having the CL code in a separate file for the compartment models and the library models. Now everything is in the Python model definition.


v0.9.38 (2017-07-25)
====================

Added
-----
- Adds Kurtosis model.
- Adds the extra-axonal time dependent CHARMED from (De Santis 2016). Still needs to be tested though.
- Adds TimeDependentZeppelin for use in the extra-axonal time dependent CHARMED model. Also, the dependency_list in the compartments now also accepts other compartments as strings. Finally, the compartments now no longer need the prefix "cm" in their CL callable function"
- Adds the ActiveAx model.
- Adds the ActiveAx model, slight update to what the Neumann cylindrical function calculates.

Changed
-------
- Small update in the model fit GUI, separated the models from the cascades to make it more clear what these mean
- Adds three new models, ActiveAx, Time Dependent ActiveAx (see De Santis 2016), Kurtosis
- Simplified the processing strategies to make it more robust
- The visualization GUI can now load images from multiple folders
- The visualization GUI now also supports dragging nifti files into the viewer for loading and viewing.
- Updates to some of the relaxometry models, fixed the simulations to the latest MOT version.

Fixed
-----
- Fixed list/dict bug in viewer.
- Fixed the simulations module to work with the latest MOT version. Updates to some of the relaxometry models.

Other
-----
- Small documentation update.
- Update to Kurtosis.
- Merge branch 'master' of github.com:cbclab/MDT.
- Merged local copy, fixed small issue in the dragging of files in the visualization GUI.
- Some initial work on the AxCaliber model. We are not there yet.
- More simplifications to the models, adds reload function in the module loaders (for reloading the cache), add TemplateModifier that can rewrite the source code of a template.
- Merge branch 'master' of github.com:cbclab/MDT.
- In the model fit GUI, separated the models from the cascades to make it more clear what the cascades do.
- In the model fit GUI, separated the models from the cascades to make it more clear what the cascades do.
- Renamed the Silvia 2016 time dependent model from CHARMED to ActiveAx.
- Made ActiveAx diffusivity dependency more clear.
- Removed the GDRCylindersFixedRadii compartment model, it was not used anywhere. Simplified the NODDI tortuosity parameter dependency.
- Update to doc about the parameter renaming.
- The parameter definitions in the compartment model now support nicknaming to enable swapping a parameter without having to rename that parameter in the model equation or other code.
- Renamed the component_configs to component templates and moved some base classes to other folders. Also, all components constructed from templates now carry a back reference to that template as a class attribute.
- Small updates to the processing strategies.
- Prepared the processing strategies for possible multithreading.
- Small comment update in the processing strategy.
- Refactored the processing strategies such that paralellization may be possible in the future.


