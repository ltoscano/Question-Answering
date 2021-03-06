from blocks.bricks import Tanh
from blocks.algorithms import BasicMomentum, AdaDelta, RMSProp, Adam, CompositeRule, StepClipping, Momentum
from blocks.initialization import IsotropicGaussian, Constant, Orthogonal

from model.index_bilinear import Model

add_cnn_data = 2.0

batch_size = 32
sort_batch_count = 20

shuffle_questions = True
shuffle_entities = True

concat_ctx_and_question = False
concat_question_before = False

embed_size = 200

ctx_lstm_size = [256, 256]
ctx_skip_connections = False

question_lstm_size = [256]
question_skip_connections = True

step_rule = CompositeRule([RMSProp(decay_rate=0.95, learning_rate=5e-5),
                           BasicMomentum(momentum=0.9)])

pos_windows = 1

dropout = 0.2
w_noise = 0.

valid_freq = 10000
save_freq = 10000
print_freq = 1000

weights_init = IsotropicGaussian(0.01)
biases_init = Constant(0.)

transition_weights_init = Orthogonal()
