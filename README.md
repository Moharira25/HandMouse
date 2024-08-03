# Hand Gesture Mouse Control

This project allows you to control your computer's mouse using hand gestures captured by your webcam. It uses computer vision techniques to track your hand movements and translate them into mouse actions.

## Features

- Move the mouse cursor using your hand
- Click by bringing your index finger and thumb together
- Double-click by performing two quick clicks
- Scroll by pinching your index finger and thumb and moving your hand up or down

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## Installation

1. Clone this repository:
2. Create and activate a virtual environment (optional but recommended):
3. Install the required packages:

## Usage

1. Run the main script:
2. Position yourself in front of your webcam, make sure one of your hands is visible.

3. Use the following gestures to control your mouse:
- Move your hand to move the cursor
- Bring your index finger and thumb together to click
- Perform two quick clicks for a double-click
- Pinch your index finger and middle finger together and move your hand up or down to scroll

4. To exit the program, you need to stop the execution of the script:
- If running from a terminal/command prompt, press Ctrl+C
- If running from an IDE, use the IDE's "Stop" or "Terminate" function

Note: The program will continue running until you manually stop the script execution.

## Customization

You can adjust various parameters in the `handTrackingModule.py` file to fine-tune the hand detection and gesture recognition:

- `maxHands`: Maximum number of hands to detect (default is 1)
- `detectionCon`: Minimum confidence threshold for hand detection (default is 0.90)
- `trackCon`: Minimum confidence threshold for hand tracking (default is 0.85)
- `threshold` in `is_pressing` method: Distance threshold to consider as a click (default is 15)

## Troubleshooting

- If the mouse movement seems inverted, check the screen coordinate calculation in `HM.py`.
- If gestures are not being recognized correctly, try adjusting the `detectionCon` and `trackCon` parameters in `handTrackingModule.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [LICENSE](LICENSE) file in the repository.

## Credits

This project was created by [Moharira25](https://github.com/Moharira25).
