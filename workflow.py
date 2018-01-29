5. Read the tutorial on nipype workflows and do the following:

Create a workflow that runs BET on 1 subject (subject 50008), and then runs FSL's FAST to segment gray and white matter, CSF. The masked brain (BET output) is what FAST should use to segment.
Create and display an image of the workflow using workflow.write_graph()

import nipype.pipeline.engine as pe
import nipype.interfaces.fsl as fsl
from nipype.interfaces import fsl
from nipype.interfaces.fsl import maths
from nipype.pipeline.engine import Workflow, Node, MapNode
from nipype.interfaces.fsl import BET

workflow = pe.Workflow(name='anaconda3')
workflow.base_dir = '~/anaconda3'
workflow.output_dir = '~/anaconda3'
mybet = pe.Node(interface=fsl.BET(), name='betnode')
mybet.inputs.in_file = "~/anaconda3/mprage.nii.gz"
mybet.inputs.out_file = "~/anaconda3/mprage_brain_mask.nii.gz"
mybet.base_dir = '~/anaconda3'
beta = mybet.run()
fast = pe.Node(interface=fsl.FAST(), name='fast')
fast.inputs.in_files = "~/anaconda3/mprage_brain_mask.nii.gz"
fast.base_dir = '~/anaconda3'
fasto = fast.run()
workflow.connect(mybet,'betnode_result', fast, 'fast_input')
workflow.write_graph()
