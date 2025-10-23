import os, math, pathlib
TEMPLATE = """<?xml version="1.0" ?>
<sdf version="1.9">
    <world name="fs_world">
        <include>
            <uri>gz://empty.sdf</uri>
        </include>
        <light name="sun" type="directional">
            <cast_shadows>true</cast_shadows>
        </light>
        <model name="ground">
            <static>true</static>
            <link name="link">
                <collision name="col">
                    <geometry>
                        <plane>
                            <normal>0 0 1</normal>
                            <size>500 500</size>
                        </plane>
                    </geometry>
                </collision>
                <visual name="vis">
                    <geometry>
                        <plane>
                            <normal>0 0 1</normal>
                            <size>500 500</size>
                        </plane>
                        <material>
                            <ambient>0.2 0.2 0.2 1</ambient>
                        </material>
                    </geometry>
                </visual>
            </link>
        </model>
    {CONES}
    </world>
</sdf>
"""

CONE = """<model name="cone_{i}">
    <pose>{x} {y} 0 0 0 0</pose>
    <static>true</static>
    <link name="link">
        <collision name="col">
            <geometry>
                <cylinder>
                    <radius>0.12</radius>
                    <length>0.35</length>
                </cylinder>
            </geometry>
        </collision>
        <visual name="vis">
            <geometry>
                <cylinder>
                    <radius>0.12</radius>
                    <length>0.35</length>
                </cylinder>
                <material>
                    <ambient>{r} {g} {b} 1</ambient>
                </material>
            </geometry>
        </visual>
    </link>
</model>
"""
def make_cones(center=(0,0), a=25.0, b=12.0, lane_w=3.0, step_deg=6):
    cx, cy = center
    cones=[]

    def color(rgb): return dict(r=rgb[0], g=rgb[1], b=rgb[2])

    blue=(0.1,0.2,0.9); yellow=(0.9,0.8,0.1)
    i=0
    for deg in range(0,360,step_deg):
        t=math.radians(deg)

        # center ellipse
        X=cx + a*math.cos(t)
        Y=cy + b*math.sin(t)

        # normal vector (approx) for lateral offset
        nx = math.cos(t)/a; ny = math.sin(t)/b
        n_norm = math.hypot(nx, ny); nx/=n_norm; ny/=n_norm

        # left/right boundaries
        XL = X + lane_w*nx
        YL = Y + lane_w*ny
        XR = X - lane_w*nx
        YR = Y - lane_w*ny

        cones.append(CONE.format(i=i,x=XL,y=YL,**color(blue)))
        i+=1
        cones.append(CONE.format(i=i,x=XR,y=YR,**color(yellow)))
        i+=1
    return "\n".join(cones)

def main():
    cones = make_cones()
    sdf = TEMPLATE.replace("{CONES}", cones)
    out = pathlib.Path(__file__).with_name("fs_oval.world")
    out.write_text(sdf)
    print("Wrote", out)

if __name__ == "__main__":
    main()
