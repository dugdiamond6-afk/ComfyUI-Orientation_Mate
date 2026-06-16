import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "OrientationMate.SnapLogic",
    async nodeCreated(node) {
        if (node.comfyClass === "OrientationMate") {
            // Find the input widget by its internal name
            const widget = node.widgets.find((w) => w.name === "New Longest Edge");
            
            if (widget) {
                const oldCallback = widget.callback;
                widget.callback = function (value) {
                    // Force the value to the nearest ceiling multiple of 16
                    const snappedValue = Math.ceil(value / 16) * 16;
                    widget.value = snappedValue;
                    
                    if (oldCallback) {
                        return oldCallback.apply(this, [snappedValue]);
                    }
                };
            }
        }
    }
});