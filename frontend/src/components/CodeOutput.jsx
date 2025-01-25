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
        minHeight: "60px",
        maxHeight: "60px",
        overflowY: "auto",
      }}
    >
      <h3 style={{
        marginBottom :"4px",
        marginTop : "4px",
      }}>Output:</h3>
      <pre
        style={{
          fontSize: "14px",
          marginTop : "0px",
          color : "#000000",
          marginLeft : "2px",
        }}
      >
        {output}
      </pre>
    </div>
  );
}

export default CodeOutput;
