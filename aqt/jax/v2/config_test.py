# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test for AQT configs."""
import difflib
import pprint
from absl.testing import absltest
from absl.testing import parameterized
from aqt.jax.v2 import config
from aqt.jax.v2.flax import aqt_flax
import jax.numpy as jnp


class AqtConfigTest(parameterized.TestCase):

  def test_config_v4(self):
    cfg = aqt_flax.config_v4(
        fwd_bits=8,
        dlhs_bits=7,
        drhs_bits=6,
        rng_type='custom-1',
        dlhs_local_aqt=config.LocalAqt(2),
        drhs_local_aqt=config.LocalAqt(3),
        fwd_accumulator_dtype=jnp.int16,
        dlhs_accumulator_dtype=jnp.int8,
        drhs_accumulator_dtype=jnp.int4,
    )
    cfg_str = pprint.pformat(cfg)
    expected_cfg_str = """DotGeneral(fwd=DotGeneralRaw(lhs=Tensor(quantizer=Quantizer(numerics=IntNumerics(bits=8,
                                                                                 preserve_zero=True,
                                                                                 preserve_max_val=False,
                                                                                 clip=True,
                                                                                 clip_gradient=False,
                                                                                 round=True,
                                                                                 noise_fn=None,
                                                                                 dtype=<class 'jax.numpy.int8'>),
                                                            calib_shared_axes=None,
                                                            scale_stop_grad=True,
                                                            calibration=AbsMaxCalibration(),
                                                            po2_scale=False,
                                                            context=Context(key=None,
                                                                            train_step=None)),
                                        use_fwd_quant=None,
                                        dequant_mode=<DequantMode.OUTPUT: 1>),
                             rhs=Tensor(quantizer=Quantizer(numerics=IntNumerics(bits=8,
                                                                                 preserve_zero=True,
                                                                                 preserve_max_val=False,
                                                                                 clip=True,
                                                                                 clip_gradient=False,
                                                                                 round=True,
                                                                                 noise_fn=None,
                                                                                 dtype=<class 'jax.numpy.int8'>),
                                                            calib_shared_axes=None,
                                                            scale_stop_grad=True,
                                                            calibration=AbsMaxCalibration(),
                                                            po2_scale=False,
                                                            context=Context(key=None,
                                                                            train_step=None)),
                                        use_fwd_quant=None,
                                        dequant_mode=<DequantMode.OUTPUT: 1>),
                             dg_accumulator_dtype=<class 'jax.numpy.int16'>,
                             local_aqt=None,
                             jax_scope_name='aqt_fwd'),
           dlhs=DotGeneralRaw(lhs=Tensor(quantizer=Quantizer(numerics=IntNumerics(bits=7,
                                                                                  preserve_zero=True,
                                                                                  preserve_max_val=False,
                                                                                  clip=True,
                                                                                  clip_gradient=False,
                                                                                  round=True,
                                                                                  noise_fn=RandomCenteredUniform(),
                                                                                  dtype=<class 'jax.numpy.int8'>),
                                                             calib_shared_axes=None,
                                                             scale_stop_grad=True,
                                                             calibration=AbsMaxCalibration(),
                                                             po2_scale=False,
                                                             context=Context(key=None,
                                                                             train_step=None)),
                                         use_fwd_quant=None,
                                         dequant_mode=<DequantMode.OUTPUT: 1>),
                              rhs=Tensor(quantizer=Quantizer(numerics=IntNumerics(bits=7,
                                                                                  preserve_zero=True,
                                                                                  preserve_max_val=False,
                                                                                  clip=True,
                                                                                  clip_gradient=False,
                                                                                  round=True,
                                                                                  noise_fn=None,
                                                                                  dtype=<class 'jax.numpy.int8'>),
                                                             calib_shared_axes=None,
                                                             scale_stop_grad=True,
                                                             calibration=AbsMaxCalibration(),
                                                             po2_scale=False,
                                                             context=Context(key=None,
                                                                             train_step=None)),
                                         use_fwd_quant=False,
                                         dequant_mode=<DequantMode.OUTPUT: 1>),
                              dg_accumulator_dtype=<class 'jax.numpy.int8'>,
                              local_aqt=LocalAqt(contraction_axis_shard_count=2),
                              jax_scope_name='aqt_dlhs'),
           drhs=DotGeneralRaw(lhs=Tensor(quantizer=Quantizer(numerics=IntNumerics(bits=6,
                                                                                  preserve_zero=True,
                                                                                  preserve_max_val=False,
                                                                                  clip=True,
                                                                                  clip_gradient=False,
                                                                                  round=True,
                                                                                  noise_fn=RandomCenteredUniform(),
                                                                                  dtype=<class 'jax.numpy.int8'>),
                                                             calib_shared_axes=None,
                                                             scale_stop_grad=True,
                                                             calibration=AbsMaxCalibration(),
                                                             po2_scale=False,
                                                             context=Context(key=None,
                                                                             train_step=None)),
                                         use_fwd_quant=None,
                                         dequant_mode=<DequantMode.OUTPUT: 1>),
                              rhs=Tensor(quantizer=Quantizer(numerics=IntNumerics(bits=6,
                                                                                  preserve_zero=True,
                                                                                  preserve_max_val=False,
                                                                                  clip=True,
                                                                                  clip_gradient=False,
                                                                                  round=True,
                                                                                  noise_fn=None,
                                                                                  dtype=<class 'jax.numpy.int8'>),
                                                             calib_shared_axes=None,
                                                             scale_stop_grad=True,
                                                             calibration=AbsMaxCalibration(),
                                                             po2_scale=False,
                                                             context=Context(key=None,
                                                                             train_step=None)),
                                         use_fwd_quant=False,
                                         dequant_mode=<DequantMode.OUTPUT: 1>),
                              dg_accumulator_dtype=<class 'jax.numpy.int4'>,
                              local_aqt=LocalAqt(contraction_axis_shard_count=3),
                              jax_scope_name='aqt_drhs'))"""

    def print_diff():
      diff_generator = difflib.context_diff(
          cfg_str.split(' '), expected_cfg_str.split(' ')
      )
      for diff in diff_generator:
        print(diff)

    assert cfg_str == expected_cfg_str, print_diff()


if __name__ == '__main__':
  absltest.main()
