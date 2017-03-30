#!/bin/bash

export CS_API_ENDPOINT=http://127.0.0.1:8080/client/api
export CS_API_KEY=kW57SlDvz2NT3P9iQR94Vurpf_1lfOgmNQ1fR_CaPpDCn0N_7yHxCIVjSVnL4irnNYHSWRI41QUonU-kRhny6A
export CS_API_SECRET=RRfrvAhJKabcHodonjdy5dT-BETONdWzVxqEuRa0NJj67DodD4NXSccGyg5UOki3B-NkTs-gZGMl7ORsA_J7zA
export DEBUG=true
export VOLUME_REMOVE_DELAY_MINUTES=10

export TAG_KEY=status
export TAG_VALUE=removed

../src/clean-objects.py