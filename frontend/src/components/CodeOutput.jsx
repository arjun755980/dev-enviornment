import React from "react";

function CodeOutput({ output }) {
  return (
    <div
      style={{
        border: "1px solid white",
        marginTop: "10px",
        padding: "10px",
        backgroundColor: "var(--third)",
        color: "#dcdcdc",
        overflow: "auto",
      }}
    >
      <h3>Output:</h3>
      <pre
        style={{
          fontSize: "12px",
          marginTop : "0px",
        }}
      >
        {output}
      </pre>
    </div>
  );
}

export default CodeOutput;
