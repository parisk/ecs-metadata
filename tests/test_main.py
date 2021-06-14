import json

import ecs_metadata


def test_extract_ips_from_metadata():
    with open("fixtures/container_metadata_v4.json") as f:
        f_contents = f.read()
        metadata = json.loads(f_contents)
        ips = ecs_metadata.extract_ips_from_metadata(metadata)
        assert ips == ["192.0.2.3"]
