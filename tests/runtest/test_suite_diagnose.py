# Testing for the 'lnt runtest test-suite --diagnose' feature.
#
# RUN: rm -rf  %t.SANDBOX  %t.SANDBOX2 || true
#

# Check --diagnose requires --only-test
# RUN: lnt runtest test-suite \
# RUN:     --sandbox %t.SANDBOX \
# RUN:     --no-timestamp \
# RUN:     --test-suite %S/Inputs/test-suite-cmake \
# RUN:     --cc %{shared_inputs}/FakeCompilers/clang-r154331 \
# RUN:     --use-cmake %S/Inputs/test-suite-cmake/fake-cmake \
# RUN:     --use-make %S/Inputs/test-suite-cmake/fake-make \
# RUN:     --use-lit %S/Inputs/test-suite-cmake/fake-lit \
# RUN:     --diagnose \
# RUN:     2>&1 | tee %t.err || echo "expected to fail"
# RUN: FileCheck  --check-prefix CHECK-ARGS < %t.err %s
# CHECK-ARGS: --diagnose requires --only-test

# Check a basic nt run.
# RUN: lnt runtest test-suite \
# RUN:     --sandbox %t.SANDBOX \
# RUN:     --no-timestamp \
# RUN:     --test-suite %S/Inputs/test-suite-cmake \
# RUN:     --cc %{shared_inputs}/FakeCompilers/clang-r154331 \
# RUN:     --use-cmake %S/Inputs/test-suite-cmake/fake-cmake \
# RUN:     --use-make %S/Inputs/test-suite-cmake/fake-diagnose-make \
# RUN:     --use-lit %S/Inputs/test-suite-cmake/fake-lit \
# RUN:     --diagnose --only-test SingleSource/Benchmarks/Stanford/Bubblesort \
# RUN:     2>&1 | tee %t.diagnose.log
# RUN: FileCheck  --check-prefix CHECK-DIAGNOSE < %t.diagnose.log %s

# CHECK-DIAGNOSE: Report produced in:
# CHECK-DIAGNOSE: Bubblesort.report
