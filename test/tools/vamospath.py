import os


def vamospath_ami2sys_cwd_test(toolrun):
  cwd = os.getcwd()
  status, out, err = toolrun.run("vamospath", "ami2sys", "")
  assert status == 0
  assert err == []
  assert out == [cwd]


def vamospath_ami2sys_error_test(toolrun):
  status, out, err = toolrun.run("vamospath", "-Vcwd:.", "ami2sys", "/")
  assert status == 1
  assert err == ["path='cwd:': can't join parent relative path"]
  assert out == []


def vamospath_sys2ami_cwd_test(toolrun):
  cwd = os.getcwd()
  status, out, err = toolrun.run("vamospath", "-Vcwd:.", "sys2ami", cwd)
  assert status == 0
  assert err == []
  assert out == ["cwd:"]


def vamospath_sys2ami_tmp_test(toolrun, tmpdir):
  p = str(tmpdir)
  status, out, err = toolrun.run("vamospath", "sys2ami", p)
  assert status == 0
  assert err == []
  assert out == ["root:" + p[1:]]