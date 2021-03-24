# Inno Setup Portable conan package

This conan package provides [Inno Setup Compiler](https://jrsoftware.org/isinfo.php).

## Usage

### With conan virtualenv 

Add a `conanfile.txt` to your project:
```
[requires]
innosetup/6.0.5-3@ci/stable 

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

```
conan create . user/channel
```

### Share the conan package
```
conan upload -r conan-local --all -c "innosetup/*@user/channel"
```
