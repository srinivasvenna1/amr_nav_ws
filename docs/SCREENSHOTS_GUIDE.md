# How to Take Screenshots and Create Demo GIFs

This guide will help you capture screenshots and create demonstration GIFs for the GitHub repository.

## 📸 Taking Screenshots

### Option 1: Using GNOME Screenshot (Ubuntu Default)

1. **Full Screen**:
   ```bash
   gnome-screenshot
   ```

2. **Specific Window**:
   ```bash
   gnome-screenshot -w
   ```
   Then click on the window you want to capture (Gazebo, RViz, etc.)

3. **Area Selection**:
   ```bash
   gnome-screenshot -a
   ```

### Option 2: Using scrot

Install if needed:
```bash
sudo apt install scrot
```

Take screenshot:
```bash
scrot screenshot.png
scrot -s area.png  # Select area
scrot -d 5 delayed.png  # 5 second delay
```

### Recommended Screenshots to Take

1. **Gazebo Simulation**
   - Launch: `ros2 launch amr_bot_gazebo launch_sim.launch.py`
   - Save as: `docs/images/gazebo_sim.png`

2. **RViz with Map Building**
   - Launch SLAM + RViz
 - Drive robot around
   - Save as: `docs/images/rviz_slam.png`

3. **Complete System**
   - All 4 terminals visible
   - Save as: `docs/images/full_system.png`

4. **Built Map**
   - RViz showing completed map
   - Save as: `docs/images/complete_map.png`

## 🎬 Creating Demo GIFs

### Option 1: Using Peek (Recommended)

1. **Install Peek**:
   ```bash
   sudo add-apt-repository ppa:peek-developers/stable
   sudo apt update
   sudo apt install peek
   ```

2. **Record GIF**:
   - Launch Peek: `peek`
   - Position the recording window over what you want to record
   - Click red record button
   - Perform your demonstration
   - Click stop
   - Save as GIF

3. **Recommended Recordings**:
   - `slam_demo.gif` - Robot driving and building map in RViz (20-30 seconds)
   - `nav_demo.gif` - Robot navigating to goal (15-20 seconds)
   - `gazebo_robot.gif` - Robot moving in Gazebo (10 seconds)

### Option 2: Using SimpleScreenRecorder + FFmpeg

1. **Install**:
   ```bash
   sudo apt install simplescreenrecorder ffmpeg
   ```

2. **Record Video**:
   - Launch SimpleScreenRecorder
   - Select area to record
   - Save as MP4

3. **Convert to GIF**:
   ```bash
   ffmpeg -i input.mp4 -vf "fps=10,scale=800:-1:flags=lanczos" -c:v gif output.gif
   ```

4. **Optimize GIF size**:
   ```bash
   sudo apt install gifsicle
   gifsicle -O3 --colors 256 output.gif -o optimized.gif
   ```

### Option 3: Using Terminalizer (For Terminal Demos)

1. **Install**:
   ```bash
   sudo npm install -g terminalizer
   ```

2. **Record**:
   ```bash
   terminalizer record demo
   # Perform your terminal commands
   # Press Ctrl+D when done
   ```

3. **Generate GIF**:
   ```bash
   terminalizer render demo
   ```

## 📋 Screenshot Checklist for GitHub

Save these images in `docs/images/`:

- [ ] `gazebo_sim.png` - Robot in Gazebo world
- [ ] `rviz_slam.png` - RViz with SLAM mapping
- [ ] `rviz_navigation.png` - RViz with navigation
- [ ] `complete_map.png` - Finished map
- [ ] `terminal_setup.png` - 4 terminals running
- [ ] `robot_model.png` - Robot model in RViz
- [ ] `lidar_scan.png` - LIDAR visualization

GIF Demos needed:

- [ ] `slam_demo.gif` - SLAM mapping process
- [ ] `nav_demo.gif` - Autonomous navigation
- [ ] `obstacle_avoidance.gif` - Robot avoiding obstacles

## 🎨 Image Guidelines

- **Resolution**: At least 1280x720 for screenshots
- **GIF Duration**: 10-30 seconds max
- **GIF Size**: Keep under 10MB (optimize if needed)
- **Format**: PNG for screenshots, GIF for animations
- **Background**: Clean, professional appearance

## 📝 Adding to README

After capturing images, update `README_GITHUB.md`:

1. Replace placeholder image links:
   ```markdown
   ![Robot Navigation Demo](docs/images/slam_demo.gif)
   ![Gazebo Simulation](docs/images/gazebo_sim.png)
   ```

2. Add image gallery section:
   ```markdown
   ## 🖼️ Gallery
   
   <p align="center">
     <img src="docs/images/gazebo_sim.png" width="45%" />
     <img src="docs/images/rviz_slam.png" width="45%" />
   </p>
   ```

## 🚀 Quick Capture Script

Save this as `capture_demos.sh`:

```bash
#!/bin/bash
echo "Starting demo capture in 5 seconds..."
sleep 5

# Capture Gazebo
gnome-screenshot -w -f docs/images/gazebo_$(date +%s).png &
echo "Click on Gazebo window"
sleep 3

# Capture RViz
gnome-screenshot -w -f docs/images/rviz_$(date +%s).png &
echo "Click on RViz window"
sleep 3

echo "Screenshots saved to docs/images/"
```

Make executable:
```bash
chmod +x capture_demos.sh
```

## 🔍 Example Commands for Demo

1. **SLAM Demo Recording Steps**:
   - Start Peek recording
   - Focus on RViz window
   - Drive robot in a pattern (square or circle)
   - Watch map build for 20-30 seconds
   - Stop recording
   - Save as `slam_demo.gif`

2. **Navigation Demo Recording Steps**:
   - Load saved map
   - Start recording
   - Send navigation goal in RViz
   - Show robot path planning
   - Show robot reaching goal
   - Stop recording
   - Save as `nav_demo.gif`

---

**Tip**: Keep GIFs short and focused on one feature at a time for better clarity!
