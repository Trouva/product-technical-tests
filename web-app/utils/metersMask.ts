export const metersMask = (distance: number) => {
  if (distance >= 1000) return Math.round(distance / 1000.0) + " km";
  if (distance >= 100) return Math.round(distance) + " m";
  return distance.toFixed(1) + " m";
};

export default metersMask;
