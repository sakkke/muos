.. raw:: html

   <h1>

.. figure:: https://socialify.git.ci/sakkke/muos/image?issues=1&language=1&name=1&owner=1&pattern=Formal%20Invitation&stargazers=1&theme=Light
   :alt: muos

   muos

.. raw:: html

   </h1>

|image1| |image2|

muOS

Links
-----

-  `CHANGELOG.rst <./CHANGELOG.rst>`__
-  `CODE_OF_CONDUCT.rst <./CODE_OF_CONDUCT.rst>`__
-  `CONTRIBUTING.rst <./CONTRIBUTING.rst>`__
-  `Documents <https://muos.netlify.app/>`__
-  `LICENSE <./LICENSE>`__

Dev
---

1. On the target:

.. code:: bash

   addr="$(ip route get 1.2.3.4 | head --lines=1 | awk '{print $7}')"
   echo "addr=$addr"
   nc -lvp 6867 | install /dev/stdin /usr/local/bin/serve

2. On the host:

.. code:: bash

   addr='<addr>'
   nc -vw 2 "$addr" 6867 < ./scripts/serve

3. On the target:

.. code:: bash

   serve

4. On the host:

.. code:: bash

   ./scripts/transfer "$addr"

.. |image1| image:: https://img.shields.io/circleci/build/github/sakkke/muos?style=for-the-badge
   :target: https://app.circleci.com/pipelines/github/sakkke/muos
.. |image2| image:: https://img.shields.io/codecov/c/github/sakkke/muos?style=for-the-badge
   :target: https://app.codecov.io/gh/sakkke/muos
