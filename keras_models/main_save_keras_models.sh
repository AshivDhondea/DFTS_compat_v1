#!/bin/bash
#SBATCH --gres=gpu:1        # request GPU "generic resource"
#SBATCH --cpus-per-task=6   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=32000M        # memory per node
#SBATCH --time=0-2:00:00      # time (DD-HH:MM)
#SBATCH --account=def-ibajic
#SBATCH --output=%j-%N.out  # %N for node name, %j for jobID

#SBATCH --mail-user=ashivdhondea5@gmail.com
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=REQUEUE
#SBATCH --mail-type=ALL

echo 'main_split_internal.sh'

echo 'Starting experiment'

echo "Starting run at: `date`"

module load cuda cudnn
source ~/scratch/tensorflow/bin/activate

python main_save_keras_models.py

echo "Ending run at: `date`"
echo 'Experiment completed!'
