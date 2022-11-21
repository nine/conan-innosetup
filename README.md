# Inno Setup Portable conan package

This conan package provides [Inno Setup Compiler](https://jrsoftware.org/isinfo.php).

## Usage

### With conan virtualenv 

Add a `conanfile.txt` to your project:
```
[requires]
innosetup/6.2.0-5@user/channel

[generators]
virtualenv
```

Call the Inno Setup compier `iscc`
```
conan install .
activate.ps1
iscc path/to/innosetup_project.iss
```

### Build the conan package

On *MS Windows* (native):
```
conan create . 6.2.0-5@user/channel
```

On GNU/Linux and other Unix variants (cross compile):
```
conan create --profile:host=host_profile --pofile:build=default . 6.2.0-5@user/channel
```

### Share the conan package
```
conan upload -r <remote-repository> --all -c "innosetup/*@user/channel"
```
