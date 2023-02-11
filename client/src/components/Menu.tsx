import React from 'react';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import FormatListBulletedIcon from '@mui/icons-material/FormatListBulleted';
import CalendarTodayIcon from '@mui/icons-material/CalendarToday';
import PersonIcon from '@mui/icons-material/Person';
import SettingsIcon from '@mui/icons-material/Settings';

function Menu() {
  return (
    <BottomNavigation className="Menu">
      <BottomNavigationAction icon={<FormatListBulletedIcon />} />
      <BottomNavigationAction icon={<CalendarTodayIcon />} />
      <BottomNavigationAction icon={<PersonIcon />} />
      <BottomNavigationAction icon={<SettingsIcon />} />
    </BottomNavigation>
  );
}

export default Menu;