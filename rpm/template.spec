Name:           ros-hydro-object-recognition-linemod
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS object_recognition_linemod package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/wg-perception/linemod
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-ecto
Requires:       ros-hydro-object-recognition-core
Requires:       ros-hydro-object-recognition-renderer
Requires:       ros-hydro-opencv-candidate
Requires:       ros-hydro-opencv2
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-ecto
BuildRequires:  ros-hydro-object-recognition-core
BuildRequires:  ros-hydro-object-recognition-renderer
BuildRequires:  ros-hydro-opencv-candidate
BuildRequires:  ros-hydro-opencv2

%description
An object recognition pipeline that uses LINE-MOD from OpenCV

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Jan 18 2015 Vincent Rabaud <vincent.rabaud@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

