
task = 'stress'
feature_set = ['egemaps']
emo_dim = 'arousal'
normalize = False
norm_opts = ['n']*len(feature_set)
win_len=300
hop_len=50
d_rnn = 64
rnn_n_layers = 4
rnn_bi = False
d_fc_out = 64
epochs = 100
batch_size = 1
seed = 103
n_seeds = 2
lr = 0.002


use_gpu = True
regularization = 0.0
eval_model = None
predict = True
save = True
save_path = 'preds'
preds_path = 'preds'
cache = True
apply_segmentation = True