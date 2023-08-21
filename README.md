# tango-extensions

[![CI](https://github.com/shunk031/tango-extensions/actions/workflows/ci.yaml/badge.svg)](https://github.com/shunk031/tango-extensions/actions/workflows/ci.yaml)
[![Release](https://github.com/shunk031/tango-extensions/actions/workflows/deploy_and_release.yaml/badge.svg)](https://github.com/shunk031/tango-extensions/actions/workflows/deploy_and_release.yaml)
![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue?logo=python)
[![PyPI](https://img.shields.io/pypi/v/tango-extensions.svg)](https://pypi.python.org/pypi/tango-extensions)

Extension modules for [`allenai/tango` (ai-2tango)](https://github.com/allenai/tango).

## Installation

tango-extensions is available [on PyPI](https://pypi.org/project/tango-extensions/). Just run:

```shell
pip install tango-extensions
```

To install with a specific integration, such as [`diffusers`](https://github.com/huggingface/diffusers) for example, run:

```shell
pip install 'tango-extensions[diffusers]'
```

To install with all integrations, run:

```shell
pip install 'tango-extensions[all]'
```

## Available Extensions

| Extension name | Integration path | Details |
|----------------|------------------|---------|
| [`huggingface/diffusers`](https://github.com/huggingface/diffusers) | [tango_ext/integrations/diffusers](https://github.com/shunk031/tango-extensions/tree/master/tango_ext/integrations/diffusers) | [diffusers/format](https://github.com/shunk031/tango-extensions/blob/master/tango_ext/integrations/diffusers/format.py)

## Acknowledgements

- allenai/tango: Organize your experiments into discrete steps that can be cached and reused throughout the lifetime of your research project. https://github.com/allenai/tango 

## License

MIT
