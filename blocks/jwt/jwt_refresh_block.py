from nio import Block
from nio.block.terminals import output
from nio.block.mixins import EnrichSignals
from nio.properties import BoolProperty, SelectProperty, StringProperty, Property, ListProperty, VersionProperty
from .jwt_base import JWTBase
import jwt

@output('valid', label='New Token')
@output('not_valid', label='Error')
class JWTRefresh(EnrichSignals, JWTBase):
    input = StringProperty(title='Token Value', default='token', order=3)
    exp = StringProperty(title='New Expiration Date', default='{{ int((datetime.datetime.now() + datetime.timedelta(minutes=60)).timestamp())) }}', order=4)
    output = StringProperty(title='Output Attribute', default='token', order=5)
    version = VersionProperty('0.1.0')

    def process_signals(self, signals, **kwargs):
        _output = self.output()
        _key = self.key()
        _algorithm = self.algorithm()
        _result = 'valid'

        output_signals = []

        for signal in signals:
            _token = self.input(signal)
            _exp = self.exp(signal)
            _claims = None

            try:
                _claims = jwt.decode(_token, _key, algorithm=_algorithm.value)
            except Exception as e:
                _result = 'not_valid'
                output_signals.append(self.get_output_signal({'error': 1, 'message': 'Could not decrypt existing token: {}'.format(e)}, signal))

            try:
                _claims['exp'] = int(_exp)
                token = jwt.encode(_claims, _key, algorithm=_algorithm.value)
                output_signals.append(self.get_output_signal({_output: token.decode('UTF-8')}, signal))

            except Exception as e:
                _result = 'not_valid'
                output_signals.append(self.get_output_signal({'error': 1, 'message': 'Could not create new token: {}'.format(e)}, signal))

        self.notify_signals(output_signals, output_id=_result)
