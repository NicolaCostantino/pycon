import * as React from 'react';

import * as styles from './style.css';

export type ColumnHeader = {
  label: string;
  accessor: string;
};

type Props = {
  columns: ColumnHeader[];
  data: object[];
};

export class Table extends React.Component<Props, {}> {
  public render() {
    const { columns } = this.props;
    return (
      <table className={styles.table} cellSpacing={0}>
        <thead>
          <tr>
            <th>Select</th>
            {columns.map(c => (
              <th key={c.label}>{c.label}</th>
            ))}
          </tr>
        </thead>
        <tbody>{this.renderBody()}</tbody>
      </table>
    );
  }

  private renderBody() {
    const { columns, data } = this.props;
    return data.map((item: any, i) => (
      <tr key={i}>
        <td />
        {columns.map(column => (
          <td key={column.label}>{item[column.accessor]}</td>
        ))}
      </tr>
    ));
  }
}
