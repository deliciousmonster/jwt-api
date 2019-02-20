from nio import Block
from nio.block.mixins import EnrichSignals
from nio.properties import PropertyHolder, StringProperty, Property, ListProperty, VersionProperty
from .jwt_base import JWTBase
import jwt
import json

class ClaimField(PropertyHolder):
    name = StringProperty(title='Name', order=0)
    value = Property(title='Value', order=1)

class JWTCreate(EnrichSignals, JWTBase):
    claims = ListProperty(ClaimField, title='Claims', order=3)
    output = StringProperty(title='Output Attribute', default='token', order=4)
    version = VersionProperty('0.1.0')

    def process_signals(self, signals, **kwargs):
        _output = self.output()
        _key = self.key()
        _algorithm = self.algorithm()

        output_signals = []

        for signal in signals:
            _claims = {}

            for claim in self.claims():
                _claims[claim.name(signal)] = claim.value(signal)

            try:
                token = jwt.encode(_claims, _key, algorithm=_algorithm.value)
                output_signals.append(self.get_output_signal({_output: token.decode('UTF-8')}, signal))
                self.logger.debug('Token created: {}'.format(token))
            except Exception as e:
                output_signals.append(self.get_output_signal(None, signal))
                self.logger.debug('Token failed: {}'.format(e))

        self.notify_signals(output_signals)
