from nio import Block
from nio.block.terminals import output
from nio.block.mixins import EnrichSignals
from nio.properties import BoolProperty, SelectProperty, StringProperty, Property, ListProperty, VersionProperty
from .jwt_base import JWTBase
import jwt

@output('valid', label='Valid')
@output('not_valid', label='Not Valid')
class JWTValidate(EnrichSignals, JWTBase):
    input = StringProperty(title='Input Attribute', default='token', order=4)
    version = VersionProperty('0.1.0')

    def process_signals(self, signals, **kwargs):
        _key = self.key()
        _algorithm = self.algorithm()
        _result = 'valid'

        output_signals = []

        for signal in signals:
            _token = self.input(signal)
            try:
                token = jwt.decode(_token, _key, algorithm=_algorithm.value)
                output_signals.append(self.get_output_signal(token, signal))
                self.logger.debug('Token valid: {}'.format(token))
            except Exception as e:
                _result = 'not_valid'
                output_signals.append(self.get_output_signal(None, signal))
                self.logger.debug('Token failed: {}'.format(e))

        self.notify_signals(output_signals, output_id=_result)
